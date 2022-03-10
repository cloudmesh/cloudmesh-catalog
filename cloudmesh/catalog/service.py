from fastapi import FastAPI
from yamldb import YamlDB
from cloudmesh.common.util import path_expand

app = FastAPI()

#filename = path_expand("~/.cloudmesh/catalog/data.yml")
#db = YamlDB(filename=filename)

@app.get("/")
def read_root():
    return {"Cloudmesh Catalog": "running"}

@app.get("/load/{directory}")
def load(directory: str):
    return {"Cloudmesh Catalog": directory}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
