import toml
import os
import subprocess
import sys
import decimal
import json

def compute_naan_total_supply(balances_toml):
    return sum(map(decimal.Decimal, balances_toml["token"]["NAAN"].values()))

def source_has_nam_balance(balances_toml, source):
    return balances_toml["token"]["NAAN"].get(source)

def main():
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <genesis_files_path> <txs_path>')
        return

    addresses = {}
    genesis_files_path = sys.argv[1]
    txs_path = sys.argv[2]

    balances_toml = toml.load(os.sep.join([genesis_files_path, 'balances.toml']))
    big_toml = {"established_account": [], "validator_account": [], "bond": []}

    decimal.getcontext().prec = 256

    initial_supply = compute_naan_total_supply(balances_toml)

    for file in filter(lambda path: path[-5:] == '.toml', os.listdir(txs_path)):
        mini_toml = toml.load(os.sep.join([txs_path, file]))

        big_toml["established_account"].extend(mini_toml["established_account"])
        big_toml["validator_account"].extend(mini_toml["validator_account"])
        big_toml["bond"].extend(mini_toml["bond"])
        addresses[mini_toml["established_account"][0]["public_keys"][0]] = mini_toml["validator_account"][0]["address"]
        amount = decimal.Decimal(mini_toml["bond"][0]["amount"])
        source = mini_toml["bond"][0]["source"]

        if source_has_nam_balance(balances_toml, source):
            # If we hit this branch, usually it means we are processing
            # a bond tx from a public key.

            # Guard against weird cases where someone has attempted to bond twice;
            # when we process a bond, we assign balances to the established accounts
            # attempting to bond. If the `source` is an established account, a validator
            # has attempted to bond twice.
            assert source.startswith('tpknam1')

            # At this point, we know the bond is coming from a public key. Check if
            # it has enough balance to bond.
            assert decimal.Decimal(balances_toml["token"]["NAAN"][source]) >= amount
        else:
            # If we hit this branch, we are either processing an established account,
            # or a public key without balance.
            
            # Assign bond amount to the established account's balance.
            balances_toml["token"]["NAAN"][source] = "{:.6f}".format(amount)

            # Retrieve the public key of the established account.
            pk = mini_toml["established_account"][0]["public_keys"][0]

            # Verify that a pk has enough balance to bond.
            initial_balances = decimal.Decimal(balances_toml["token"]["NAAN"][pk])
            new_balance = initial_balances - amount
            assert new_balance >= 0

            # Subtract the bonded amount from the pk's balance.
            balances_toml["token"]["NAAN"][pk] = "{:.6f}".format(new_balance)

    # Validate the total supply of NAAN
    assert initial_supply == compute_naan_total_supply(balances_toml)

    # Update the toml files
    toml.dump(big_toml, open(os.sep.join([genesis_files_path, 'transactions.toml']), 'w'))
    toml.dump(balances_toml, open(os.sep.join([genesis_files_path, 'balances.toml']), 'w'))
    
    
    json.dump(addresses, open(os.sep.join([genesis_files_path, 'addresses.json']), 'w'))

    os.system("python3 scripts/make_whitelist.py")

if __name__ == '__main__':
    main()