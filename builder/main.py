import os

import yaml
import pystache

from loader import Loader

dirpath = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dirpath, "database", "main.yaml"), "r") as f:
    data = yaml.load(f, Loader)

with open(os.path.join(dirpath, "template.html"), "r") as f:
    parsed_template = pystache.parse(f.read())

html = pystache.render(parsed_template, data)

with open("index.html", "w") as f:
    f.write(html.strip())
