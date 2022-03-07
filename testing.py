from saildb import load, dump

with open("hello.sail", "w") as f:
    f.write(dump({"array": [1, 2, 3, 4, 5, 6]}))

with open("hello.sail") as f:
    data = load(f.read())

print(data)