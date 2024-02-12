# The Namada Shielded Expedition

Welcome to the Namada shielded expedition!

Here is where Namada pilots and crew members will expect to find the `balances.toml` file that allocates `NAAN` to public keys.

Using this `balances.toml` file, the included participants can generate and submit their **signed** pre-genesis *bonding* transactions in the `transactions` folder. These will be validated against, and only merged once the validation has passed.

Participants may bond ***up to*** the amount allocated to their public key. It is recommended not to bond the full allocation, as having `NAAN` to pay for gas will be useful. Any bonds greater than one's allocation will be rejected.

## Seeds
Syncing a new node may not work if the peers of other nodes are filled up, so participants should use (and consider making) seed nodes. Here is a list of seeds:
- `tcp://9202be72cfe612af24b43f49f53096fc5512cd7f@194.163.172.168:26656` (Mandragora)
- `tcp://2cdf24141644ef9e50ab270e7cf61c661e105d90@seeds.cryptosj.net:12904` (CryptoSJnet)
- `tcp://0edfd7e6a1a172864ddb76a10ea77a8bb242759a@65.21.194.46:36656` (adrian)

## Full Nodes
Syncing a new node may not work if the peers of other nodes are filled up, so participants should use (and consider making) full nodes. Here is a list of full nodes:
- `tcp://0c4ce0c5ceb022564b111a4e4d0c0a66a9567dbe@65.109.117.113:26656` (CroutonDigital)
- `tcp://50e15e1639476ddc091d39c7e6faf4a1a3798235@38.242.152.80:26656` (EmberStake)
- `tcp://f47f2d1fd83f8063571145f90e984a74cba6310f@65.21.194.46:26656` (adrian)
- `tcp://7a3ce1bd42d8b2e09a21377f9cc2562b59f574a6@185.84.224.125:20056` (WhisperNode)
- `tcp://b1edad170073d82537aaf3177e5042d857956adf@162.250.127.226:26656` (Brightlystake)
- `tcp://52dc61ef963ddeaee15ff358b133fceb8eff5aa3@162.55.0.160:26656` (gnosed)
- `tcp://f426c9a6287e2c2181ad64139c0963a07aea8b2a@65.108.147.137:26656` (ZKValidator)
- `tcp://b7c3c9c98dc44880be42a4437e93e3330032ae19@135.125.189.84:26656` (B-Harvest)
- `tcp://d4d14a3a8879527e42753d1bff8a69c12b4f3cd7@194.163.166.56:26656` (Mandragora)
  
## Creating the genesis files (advanced)
In order to create the genesis files for the expedition, the following steps were taken.
1. The signed transactions files were collected in the `signed_genesis_transactions` folder.
2. The python script in `scripts/txs_toml.py` was run from the root with `python3 scripts/txs_toml.py ./ ./signed_genesis_transactions` to generate the `transactions.toml` and to populate the whitelists in the `parameters.toml` file. Once this was done, it was possible to generate the chain-id.

## How to create the chain-id from the genesis files

Make sure you have the namada binaries installed and are of version `v0.31.0`. Assuming the path to the namada client binary is `$NAMADAC`, you can run the following command to generate the chain-id:

```bash
$NAMADAC utils init-network --chain-prefix shielded-expedition --genesis-time 2024-02-01T18:00:00Z --templates-path ./ --wasm-checksums-path ./utils/checksums.json --consensus-timeout-commit 10s
```
