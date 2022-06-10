from fastapi import FastAPI

import nest_asyncio
nest_asyncio.apply()

app = FastAPI()

@app.get('/hello')
def hello():
    return {'msg':'hello'}