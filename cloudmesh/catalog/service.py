from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Cloudmesh Catalog": "running"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
