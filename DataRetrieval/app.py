from Persister.mongo_dal import MongoDal
from fastapi import FastAPI
import uvicorn

app = FastAPI()
dal = MongoDal()

@app.get("/antisemitic")
def get_antiseitic():
    data = dal.get_antisemitic_docs()
    return data

@app.get("/not_antisemitic")
def get_not_antisemitic():
    data = dal.get_not_antisemitic_docs()
    return data

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
