import asyncio

import uvicorn as uvicorn
from fastapi import FastAPI
import nest_asyncio

from controller_impl import ControllerImpl

app = FastAPI()
nest_asyncio.apply()

@app.get('/hello')
def hello():
    return {'msg': 'hello'}

controller_impl = ControllerImpl()

@app.get('/links')
async def get_links():
    r = await controller_impl.get_links()
    return {'msg':'ok'}





if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, debug=True)
