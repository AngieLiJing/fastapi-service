import asyncio
from time import time

import uvicorn as uvicorn
from fastapi import FastAPI

from controller_impl import ControllerImpl

app = FastAPI()


@app.get('/hello')
def hello():
    return {'msg': 'hello'}

controller_impl = ControllerImpl()




@app.get('/')
async def f():
    start = time()
    res = await controller_impl.task()
    print("time: ", time() - start)
    return {'res': res}





if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, debug=True)
