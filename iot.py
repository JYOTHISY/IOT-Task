import json
from jinja2 import Environment
from jinja2 import FileSystemLoader

with open("data.json","r") as d:
    data=json.load(d)

for item in data:
    print(item[1])