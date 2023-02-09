import json
block = {"a": "apple", "b": "ball", "c": "Cat", "d": "Dog"}
to_json = json.dumps(block)

f = open('file.json', "w")
f.write(to_json)

f = open('file.json', "r")
print(f.read())
