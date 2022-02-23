# python examples/CloudmeshTestServer.py
# curl  http://localhost:8127/item/a
# curl  http://localhost:8127


from yamldb.YamlDB import YamlDB
import uvicorn
from fastapi import FastAPI


filename = "test.yaml"

app = FastAPI(title='CloudmeshCatalog')


@app.get("/")
def read_root():
    return {"Hello": "Cloudmesh Catalog"}

@app.get("/item/{name}")
def read_item(name: str):
    global db
    result = db.search(name)
    return {
        name: result
    }

def setup_db():
    global db
    db = YamlDB(filename="./test.yml")
    for i in ["a", "b", "c"]:
        db[i] = f"vaue  of {i}"
    db.save()

setup_db()


def start_server():
    uvicorn.run("CloudmeshTestServer:app",
                host='127.0.0.1',
                port=8127,
                workers=2)


if __name__ == '__main__':
    start_server()
