import toml
import json

p = toml.load('parameters.toml')

j = json.load(open("utils/checksums.json"))

vp_whitelist = []
tx_whitelist = []


for v in j.values():
    name, hash = v.split('.')[:2]
    if name.startswith('vp'):
        vp_whitelist.append(hash)
    elif name.startswith('tx'):
        tx_whitelist.append(hash)

p["parameters"]["vp_allowlist"] = vp_whitelist
p["parameters"]["tx_allowlist"] = tx_whitelist

toml.dump(p, open('parameters.toml', 'w'))