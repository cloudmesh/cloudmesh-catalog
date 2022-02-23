# python examples/CloudmeshTestServer.py

import uvicorn
from fastapi import FastAPI
from typing import Optional

app = FastAPI(title='CloudmeshCatalog')


@app.get("/")
def read_root():
    return {"Hello": "Cloudmesh Catalog"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run("CloudmeshTestServer:app",
                host='127.0.0.1',
                port=8127,
                workers=2)

