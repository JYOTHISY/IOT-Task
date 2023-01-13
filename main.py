import json
from jinja2 import Environment
from jinja2 import FileSystemLoader

with open("data.json","r") as d:
    data=json.load(d)

  

fileLoader=FileSystemLoader("templates")
env=Environment(loader=fileLoader)

rendered=env.get_template("iot.html").render(data=data)


fileName="index.html"

with open(f"./site/{fileName}","w") as f:
    f.write(rendered)