import json

with open(f"data.json", "r", encoding="utf-8") as f:
    m = json.load(f)

data = {}
type = ["key", "legendary", "epic", "rare", "uncommon", "common", "garbage"]

for rod in m:
    c_weights = [m[rod][weight] for weight in m[rod]]
    _sc = sum(weight for weight in c_weights)
    n_weights = [c / _sc for c in c_weights]
    for i, val in enumerate(n_weights):
        if rod not in data:
            data[rod] = {}
        data[rod][type[i]] = val

with open(f"data.json", "w") as f:
    f.write(json.dumps(data, indent=1))
