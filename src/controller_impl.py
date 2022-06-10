import asyncio

import aiohttp

URL = "http://httpbin.org/uuid"

class ControllerImpl:

    async def request(self,session):
        async with session.get(URL) as response:
            return await response.text()

    async def task(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.request(session) for i in range(100)]
            result = await asyncio.gather(*tasks)
            print(result)
            return result