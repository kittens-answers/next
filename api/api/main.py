from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_item():
    return {"method": "get"}


@app.post("/")
def read_item_():
    return {"method": "post", "payload": "api data"}
