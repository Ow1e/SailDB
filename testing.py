from saildb import load, dump
from datetime import datetime
from random import randint
from tqdm import tqdm

def generate():
    return {
        "name": "Owen Shaule",
        "email": "ow1e3@protonmail.com",
        "time": str(datetime.now()),
        "random": randint(1, 100000)
    }

data = {"row": []}
num = int(input("Rows: "))
for i in tqdm(range(num)):
    data["row"].append(generate())

print("Testing generate speed")
p = tqdm([1], total=num)
for i in p:
    text = dump(data)
    p.update(num)

with open("stuff.sail", "w") as f:
    f.write(text)

with open("stuff.json", "w") as f:
    import json
    json.dump(data, f)