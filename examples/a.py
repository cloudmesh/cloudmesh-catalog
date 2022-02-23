# python examples/CloudmeshTestServer.py
# curl  http://localhost:8127/item/a
# curl  http://localhost:8127


import glob

import uvicorn
import yaml
from fastapi import FastAPI

from cloudmesh.common.util import path_expand
from cloudmesh.common.util import readfile
from yamldb.YamlDB import YamlDB

filename = "test.yaml"

app = FastAPI(title='CloudmeshCatalog')

def load(directory="./data/catalog"):
    global db
    db = YamlDB(filename="./test.yml")
    filenames = glob.glob(path_expand(directory))
    for name in filenames:
        print(f"Loading: {name}")
        data = yaml.safe_load(readfile(name).strip())
        db[name] = data

load(directory="./data/catalog/*.yaml")

@app.get("/")
def read_root():
    return {"Message": "Cloudmesh Catalog"}

@app.get("/item/{name}")
def read_item(name: str):
    global db
    result = db.search(name)
    return {
        name: result
    }

@app.get("/item")
def read_items():
    global db
    result = db.yaml()
    return result


#def setup_db():
#    global db
#    db = YamlDB(filename="./test.yml")
#    for i in ["a", "b", "c"]:
#        db[i] = f"value  of {i}"
#    db.save()
#setup_db()


