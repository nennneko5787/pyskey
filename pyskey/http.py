import aiohttp
import asyncio
import json

class HTTP():
    def __init__(
        self,
        address: str,
        token: str,
        loop: asyncio.AbstractEventLoop = None
    ):
        self.address = address
        self.token = token
        self._loop = loop or asyncio.get_event_loop()
        self._http = aiohttp.ClientSession(loop=self._loop)

    async def post(
        self,
        address: str,
        data: dict = {}
    ):
        """
        POSTリクエストを送信します。
        """
        data.setdefault("i", self.token)
        _data = json.dumps(data)
        headers={"Content-Type": "application/json"}
        async with self._http.post(address, headers=headers, data=_data) as response:
            return (await response.json(), response.status)

    async def close(self):
        """
        HTTPセッションをクローズします。
        プログラム終了時に自動で呼び出されるため、手動で呼び出すのはお勧めしません。
        """
        await self._http.close()
