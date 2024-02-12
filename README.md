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
- `tcp://8e81eb6d4bc86066ebe0b11519333f635437733c@65.108.100.57:26656` (Nodiums)
- `tcp://9f7d037b6f6757d3ba6352d672b69b42b3e96126@54.195.152.187:26656` (Gian)

```bash
seeds = "tcp://9202be72cfe612af24b43f49f53096fc5512cd7f@194.163.172.168:26656,tcp://2cdf24141644ef9e50ab270e7cf61c661e105d90@seeds.cryptosj.net:12904,tcp://0edfd7e6a1a172864ddb76a10ea77a8bb242759a@65.21.194.46:36656,tcp://8e81eb6d4bc86066ebe0b11519333f635437733c@65.108.100.57:26656"
```

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
- `tcp://0a4ae55f81a2d5541c9f96274d1e51b1078c99df@167.235.35.48:26656` (max-01)
- `tcp://6bf567f926a18f95d5ea45837af189e3f5bd6f04@rpc-1.namada.nodes.guru:26656` (Nodes.Guru)
- `tcp://38afb25360d9a698caf5a8934f4484e676352b8e@89.58.28.79:26656` (OriginStake)
- `tcp://f6efa383790ad014f0bf9394ec39d19f4f7e0f86@65.108.76.33:33356` (StakePool)
- `tcp://ff0269406b70b76b991c8eb89918042554ecc26d@65.108.13.212:26656` (pro-nodes75)
- `tcp://9f7d037b6f6757d3ba6352d672b69b42b3e96126@54.195.152.187:26656` (gian)
- `tcp://a55591635f84e0aff9b1567d0276fe32794e5ccf@65.109.28.34:26656` (StakeUp)
- `tcp://407240435312de546dd622f4228fbc6faccc8093@88.198.62.53:26656` (PathrockNetwork)
- `tcp://53761db95fdb175ead7981ae5b92d6770f846e2f@37.27.63.150:26656` (FelesGATADAO)
- `tcp://130efdc964211249504c64b83fdda4511239596e@88.198.54.190:26656` (BlockHunters)
- `tcp://e6542c7f53d2b3bc0754f6a14b1533fcca64ef2b@147.135.65.3:26656` (jasondavies)
- `tcp://d4d14a3a8879527e42753d1bff8a69c12b4f3cd7@194.163.166.56:26656` (Mandragora)
- `tcp://783b88ab64a99d0efd7e077ecd3f1c9f787edab1@164.132.206.199:28656` (Validatorade)

```bash
persistent_peers = "tcp://0c4ce0c5ceb022564b111a4e4d0c0a66a9567dbe@65.109.117.113:26656,tcp://50e15e1639476ddc091d39c7e6faf4a1a3798235@38.242.152.80:26656,tcp://f47f2d1fd83f8063571145f90e984a74cba6310f@65.21.194.46:26656,tcp://7a3ce1bd42d8b2e09a21377f9cc2562b59f574a6@185.84.224.125:20056,tcp://b1edad170073d82537aaf3177e5042d857956adf@162.250.127.226:26656,tcp://52dc61ef963ddeaee15ff358b133fceb8eff5aa3@162.55.0.160:26656,tcp://f426c9a6287e2c2181ad64139c0963a07aea8b2a@65.108.147.137:26656,tcp://b7c3c9c98dc44880be42a4437e93e3330032ae19@135.125.189.84:26656,tcp://0a4ae55f81a2d5541c9f96274d1e51b1078c99df@167.235.35.48:26656,tcp://6bf567f926a18f95d5ea45837af189e3f5bd6f04@rpc-1.namada.nodes.guru:26656,tcp://38afb25360d9a698caf5a8934f4484e676352b8e@89.58.28.79:26656,tcp://f6efa383790ad014f0bf9394ec39d19f4f7e0f86@65.108.76.33:33356,tcp://ff0269406b70b76b991c8eb89918042554ecc26d@65.108.13.212:26656,tcp://9f7d037b6f6757d3ba6352d672b69b42b3e96126@54.195.152.187:26656,tcp://a55591635f84e0aff9b1567d0276fe32794e5ccf@65.109.28.34:26656,tcp://407240435312de546dd622f4228fbc6faccc8093@88.198.62.53:26656,tcp://53761db95fdb175ead7981ae5b92d6770f846e2f@37.27.63.150:26656,tcp://130efdc964211249504c64b83fdda4511239596e@88.198.54.190:26656,tcp://e6542c7f53d2b3bc0754f6a14b1533fcca64ef2b@147.135.65.3:26656,tcp://d4d14a3a8879527e42753d1bff8a69c12b4f3cd7@194.163.166.56:26656,tcp://783b88ab64a99d0efd7e077ecd3f1c9f787edab1@164.132.206.199:28656"
```
  
## Creating the genesis files (advanced)
In order to create the genesis files for the expedition, the following steps were taken.
1. The signed transactions files were collected in the `signed_genesis_transactions` folder.
2. The python script in `scripts/txs_toml.py` was run from the root with `python3 scripts/txs_toml.py ./ ./signed_genesis_transactions` to generate the `transactions.toml` and to populate the whitelists in the `parameters.toml` file. Once this was done, it was possible to generate the chain-id.

## How to create the chain-id from the genesis files

Make sure you have the namada binaries installed and are of version `v0.31.0`. Assuming the path to the namada client binary is `$NAMADAC`, you can run the following command to generate the chain-id:

```bash
$NAMADAC utils init-network --chain-prefix shielded-expedition --genesis-time 2024-02-01T18:00:00Z --templates-path ./ --wasm-checksums-path ./utils/checksums.json --consensus-timeout-commit 10s
```
