# The Namada Shielded Expedition

Welcome to the Namada shielded expedition!

Here is where Namada pilots and crew members will expect to find the `balances.toml` file that allocates `NAAN` to public keys.

Using this `balances.toml` file, the included participants can generate and submit their **signed** pre-genesis _bonding_ transactions in the `transactions` folder. These will be validated against, and only merged once the validation has passed.

Participants may bond **_up to_** the amount allocated to their public key. It is recommended not to bond the full allocation, as having `NAAN` to pay for gas will be useful. Any bonds greater than one's allocation will be rejected.

## Seeds

Syncing a new node may not work if the peers of other nodes are filled up, so participants should use (and consider making) seed nodes. Here is a list of seeds:

- `tcp://9202be72cfe612af24b43f49f53096fc5512cd7f@194.163.172.168:26656` (Mandragora)
- `tcp://2cdf24141644ef9e50ab270e7cf61c661e105d90@seeds.cryptosj.net:12904` (CryptoSJnet)
- `tcp://8e81eb6d4bc86066ebe0b11519333f635437733c@65.108.100.57:26656` (Nodiums)
- `tcp://9f7d037b6f6757d3ba6352d672b69b42b3e96126@54.195.152.187:26656` (Gian)
- `tcp://fd5073f30457198be3c7062dca6623b51c7e74ee@namada-testnet-seed.itrocket.net:33656` (itrocket)
- `tcp://392a9f700cfe3e88a17e8dbfdc21c626c9d96e86@173.249.11.5:26656` (manueldb2)
- `tcp://20e1000e88125698264454a884812746c2eb4807@testnet-seeds.lavenderfive.com:20056` (Lavender.Five Nodes)
- `tcp://171772a9a13f2adc6e02ef5d9c02fd18272b8d2b@135.181.135.38:26656` (Stake&Relax)
- `tcp://476f41eb60074cb603558c271470e807c39dd8bf@207.244.253.244:26656` (cryptobtcbuyer)
- `tcp://5be8ecf93ce471c6c1b6af9b7cfe0a1dde7462fa@135.125.189.60:32656` (B-Harvest)
- `tcp://61ce3d7980aaea95e5b56566c727955b1184ccbc@namada-se-seeds.emberstake.xyz:41656` (EmberStake)
- `tcp://03b452b8bf5f49283a289c411483ac12b7b86749@194.163.132.38:26656` (Daviduok)
- `tcp://679232a0ca3a830cd89992816c1e5fadcd772743@135.181.32.162:26656` (DTEAM)
- `tcp://ec1c53ae10cc9ad8e798c884aa5e1e42cab473db@43.157.88.96:26656` (P2P.ORG)

```bash
seed_nodes = "tcp://9202be72cfe612af24b43f49f53096fc5512cd7f@194.163.172.168:26656,tcp://2cdf24141644ef9e50ab270e7cf61c661e105d90@seeds.cryptosj.net:12904,tcp://0edfd7e6a1a172864ddb76a10ea77a8bb242759a@65.21.194.46:36656,tcp://8e81eb6d4bc86066ebe0b11519333f635437733c@65.108.100.57:26656"
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
- `tcp://ec6bf7cfa3ffb6f915684e3660896f7a13a27223@135.125.189.84:33656` (B-Harvest)
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
- `tcp://38226f5221e5bd1bd97fa7d343cff19bef1ad02b@34.32.21.96:26656` (Keplr)
- `tcp://da1d9d2e2ce7445f7cc5ba0ddf46b1026d5a17dd@195.201.197.246:26656` (Citizen Web3)
- `tcp://d9e2d1ce049401880e8b4eb97fb3a96ce5a72ce0@65.21.225.60:28656` (goto5k)
- `tcp://11bd97c7107505ebe6ff37b5ce2fca1847120d6c@146.59.149.91:26656` (Forest)
- `tcp://66ee66185dcaf6f60e872521fcc7e93d9b32c434@43.131.63.125:26656` (P2P.ORG)
- `tcp://cfdf31beafc3408a07194875c647da6a737c5520@65.108.68.214:28656` (DRAGONVN)
- `tcp://42d3d815638e34ee8625e88713d4c31bee9ba490@88.99.3.143:26609` (spidey)
- `tcp://53c597a8ef7d237ed829edcbb708df654a70381c@135.181.215.152:26656` (Node Guardians)

```bash
persistent_peers = "tcp://0c4ce0c5ceb022564b111a4e4d0c0a66a9567dbe@65.109.117.113:26656,tcp://50e15e1639476ddc091d39c7e6faf4a1a3798235@38.242.152.80:26656,tcp://f47f2d1fd83f8063571145f90e984a74cba6310f@65.21.194.46:26656,tcp://7a3ce1bd42d8b2e09a21377f9cc2562b59f574a6@185.84.224.125:20056,tcp://b1edad170073d82537aaf3177e5042d857956adf@162.250.127.226:26656,tcp://52dc61ef963ddeaee15ff358b133fceb8eff5aa3@162.55.0.160:26656,tcp://f426c9a6287e2c2181ad64139c0963a07aea8b2a@65.108.147.137:26656,tcp://b7c3c9c98dc44880be42a4437e93e3330032ae19@135.125.189.84:26656,tcp://0a4ae55f81a2d5541c9f96274d1e51b1078c99df@167.235.35.48:26656,tcp://6bf567f926a18f95d5ea45837af189e3f5bd6f04@rpc-1.namada.nodes.guru:26656,tcp://38afb25360d9a698caf5a8934f4484e676352b8e@89.58.28.79:26656,tcp://f6efa383790ad014f0bf9394ec39d19f4f7e0f86@65.108.76.33:33356,tcp://ff0269406b70b76b991c8eb89918042554ecc26d@65.108.13.212:26656,tcp://9f7d037b6f6757d3ba6352d672b69b42b3e96126@54.195.152.187:26656,tcp://a55591635f84e0aff9b1567d0276fe32794e5ccf@65.109.28.34:26656,tcp://407240435312de546dd622f4228fbc6faccc8093@88.198.62.53:26656,tcp://53761db95fdb175ead7981ae5b92d6770f846e2f@37.27.63.150:26656,tcp://130efdc964211249504c64b83fdda4511239596e@88.198.54.190:26656,tcp://e6542c7f53d2b3bc0754f6a14b1533fcca64ef2b@147.135.65.3:26656,tcp://d4d14a3a8879527e42753d1bff8a69c12b4f3cd7@194.163.166.56:26656,tcp://783b88ab64a99d0efd7e077ecd3f1c9f787edab1@164.132.206.199:28656,tcp://cfdf31beafc3408a07194875c647da6a737c5520@65.108.68.214:28656"
```

## Public Indexer endpoints

Indexer endpoints

- `https://namada-api.kzvn.xyz/api` (DRAGONVN)
- `http://namada-indexer.spidey.services` (spidey)
- `tcp://f9701153dddc901bbe39b4d7305c1b4e8f2f83d9@164.132.206.199:26656` (didbit)
- `tcp://e503a9c84f0997ca9da1f2aae5969fff94b341f5@142.132.197.215:26656` (Redbooker)
- `tcp://e77f9559b91a81710e854d590d128bef932e0327@168.119.5.125:31656` (AlexZ)
- `tcp://a6ff4b0836255a41a0bab456ae42fcc98ed49684@namada.rpc.lankou.org:26657` (Lankou)
- `tcp://3aaba2c749072cb49a42d34a14296d05c27aaea9@namada-testnet-peer.itrocket.net:33656` (itrocket)
- `tcp://d5edca779487a5cf4800ac26f65be7fe7a0fc903@149.28.146.7:26656` (Chainbase)
- `tcp://ea1ace5ec14b81f17862d6dc45a9a99595b0ce02@37.27.58.236:26656` (Nodeify)
- `tcp://3b8e58431ee4b331c2e4bc0763caa5364cd56ed9@95.217.203.60:26656` (ValidatorVN)
- `tcp://a6feb23e7178791a6f8d4aab4637951b511d71d6@81.200.154.160:26656` (deNodes)
- `tcp://431fe43b4868867e37701f3ab8ad576f335714fb@namada-se-rpc.contributiondao.com:26656` (ContributionDAO)
- `tcp://a31b7a31e553be1dc90c723474b79515f7c7644d@162.55.246.223:26656` (InfraDAO)
- `tcp://fc1e024c8d27cb769d158b0d7bd7a46572238d4a@95.179.137.86:26656` (DSRVLabs)
- `tcp://5cf9dbf4cf43d0bd8c9e77d05b2b1db9e86b60e9@seed-namada-shielded-expedition-01.stakeflow.io:28003` (Stakeflow)
- `tcp://aa77f29e98af6b079abd32e2cc00cd012d571c9b@65.109.89.5:28656` (2pilot)
- `tcp://f28adbd7f101fc627c8f5969c33e39635efe3a57@65.108.131.189:1337` (BlackBlocks)
- `tcp://8dc2223de13c3f2c58102dff3b1255f7063730aa@65.108.199.79:26104` (WayneWayner)
- `tcp://583790d9c077619ec822f83992d19ab074aec574@154.91.1.75:26656` (Forbole)
- `tcp://c2d0b83418f6fb8b780f6bbdbdc2e0719f967824@158.220.127.197:26656` (UniqNodes)
- `tcp://1fc8eb5685ea76faf20df5ed35d7622657e91b04@45.132.246.138:26656` (CosmicValidator)
- `tcp://fb06663d96ee935816a8494fee4d81c0546a3731@217.197.107.144:26656` (StoneMac65)

## Validator Miss Dashboard

- https://cosmostation.github.io/namadatools/

## Explorers

- `https://namada-explorer.stakepool.dev.br/` (StakePool)
- `https://extended-nebb.kintsugi.tech/` (Kintsugi)
- `https://namada-explorer.dsrvlabs.dev/` (DSRVLabs)
- `https://namadafinder.cryptosj.net/`  (CryptoSJnet)

## RPCs

- `https://namada-testnet-rpc.bwarelabs.com/` (BwareLabs)
- `https://namada-explorer-api.stakepool.dev.br/` (StakePool)
- `https://rpc-namada.kintsugi-nodes.com/` (Kintsugi)
- `https://namada-se100-rpc.gatadao.com/` (GATADAO)
- `https://namada-shielded-expedition-rpc.denodes.xyz/` (deNodes)
- `https://namada-se-rpc.citadel.one/` (CitadelOne)
- `https://namada-rpc.dsrvlabs.dev/` (DSRVLabs)
- `https://rpc-namada-se.lgns.net/` (Luganodes)
- `https://rpc.namada-expedition.tm.p2p.org/` (P2P.ORG)
- `https://rpc.namada-expedition.tm.p2p.world/` (P2P.ORG)
- `http://173.212.245.122:26657/` (didbit)
- `https://rpc-namada.cosmostation.io` (Cosmostation)
- `http://173.212.245.122:26657/`  (didbit)
- `https://namadarpcse.cryptosj.net/` (CryptoSJnet)
- `https://namada-se-rpc.contributiondao.com` (ContributionDAO)
- `https://namada-se.emberstake.xyz/` (EmberStake)
- `https://namada-rpc.kzvn.xyz` (DRAGONVN)
- `http://namada-rpc.spidey.services` (spidey)
- `https://rpc-namada.civetbera.io` (superpool)
- `http://161.97.103.23:26657/` (Capperi96)
## Indexers

- `https://namada-testnet-indexer.bwarelabs.com/` (BwareLabs)
- `https://namada-explorer-api.stakepool.dev.br/node/api-docs/#/` (StakePool)
- `https://namada-indexer.kintsugi-nodes.com/` (Kintsugi)
- `https://namada-indexer.denodes.xyz/block/last` (deNodes)
- `https://namada-se-indexer.citadel.one/` (CitadelOne)
- `https://namada-indexer.dsrvlabs.dev/` (DSRVLabs)
- `http://namadafinder.cryptosj.net:30303/` (CryptoSJnet)
- `https://api-namada.cosmostation.io` (Cosmostation)
- `https://indexer-namada.civetbera.io` (superpool)

## Snapshot service

- `https://bwarelabs.com/snapshots/namada` (BwareLabs)

## Creating the genesis files (advanced)

In order to create the genesis files for the expedition, the following steps were taken.

1. The signed transactions files were collected in the `signed_genesis_transactions` folder.
2. The python script in `scripts/txs_toml.py` was run from the root with `python3 scripts/txs_toml.py ./ ./signed_genesis_transactions` to generate the `transactions.toml` and to populate the whitelists in the `parameters.toml` file. Once this was done, it was possible to generate the chain-id.

- `http://namada.stonemac65.xyz` (StoneMac65)

## Public Indexer

- `http://namada.blog` (StoneMac65)

## Explorer

- `http://namada.blog` (StoneMac65)

## How to create the chain-id from the genesis files

Make sure you have the namada binaries installed and are of version `v0.31.0`. Assuming the path to the namada client binary is `$NAMADAC`, you can run the following command to generate the chain-id:

```bash
$NAMADAC utils init-network --chain-prefix shielded-expedition --genesis-time 2024-02-01T18:00:00Z --templates-path ./ --wasm-checksums-path ./utils/checksums.json --consensus-timeout-commit 10s
```
