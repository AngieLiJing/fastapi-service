import asyncio
import ssl

import aiohttp
import nest_asyncio
from fastapi import HTTPException
from starlette import status


class ControllerImpl:

    async def get_links(self):
        # session = aiohttp.ClientSession()
        async with aiohttp.ClientSession() as session:
            loop = asyncio.get_event_loop()

            # queries1 = [loop.create_task(self._get_chart_link(EmbeddedChartUrlIn(**query_doc), session)) for query_doc in query_docs]
            queries = [loop.create_task(self._get_link(1,session))]
            loop.run_until_complete(asyncio.gather(*queries))
            # await session.close()
            return 'a'
    async def _get_link(self,x,session):
        # async with aiohttp.ClientSession as session:
        async with session.get(url='http://www.baidu.com', ssl=ssl.SSLContext()) as resp:
            if resp.status not in [200]:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='xx')
            else:
                r = await resp.text()
            return r