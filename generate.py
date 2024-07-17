import os

import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
os.makedirs("dist", exist_ok=True)

with open("./langs/en.yaml", encoding="utf-8") as f:
    base_lang = yaml.safe_load(f)

for file in os.listdir("langs"):
    if os.path.isfile(os.path.join("langs", file)):
        if file.endswith(".yaml") or file.endswith(".yml"):
            with open(os.path.join("langs", file), "r", encoding="utf-8") as f:
                langFile = yaml.safe_load(f)
                lang_nmld = {**langFile, **base_lang}
                template = env.get_template("home.html")
                if langFile['lang'] != "en":
                    with open(os.path.join(os.path.join("dist", {langFile['lang']}), "index.html"), "w", encoding="utf-8") as f:
                        f.write(template.render(**lang_nmld))
                else:
                    with open(os.path.join("dist", "index.html"), "w", encoding="utf-8") as f:
                        f.write(template.render(**lang_nmld))