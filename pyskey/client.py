import asyncio
import aiohttp
from .type.medetailed import MeDetailed
from types import FunctionType

class Event:
	def __init__(self, func):
		self.func = func

	def __get__(self, instance, owner):
		return self if instance is None else self.wrapper(instance)

	def wrapper(self, instance):
		async def wrapped(*args, **kwargs):
			return await self.func(instance, *args, **kwargs)
		return wrapped

class Client:
	"""
	Pyskeyのクライアントクラス。
	以下の方法で呼び出すことを推奨します。
	```
	client = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")
	```
	クラスを継承する方法でも呼び出せるかもしれません。(未検証)

	イベントを追加するには、デコレータを使用するか、add_event関数を使用します。
	```
	client = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")

	# デコレータを使う方法
	@client.event
	async def on_ready():
		print(f"{client.me.name} ( {client.me.username} ) にログインしました - デコレータ")

	# add_event関数を使う方法
	async def ready_event():
		print(f"{client.me.name} ( {client.me.username} ) にログインしました - add_event関数")
	add_event("on_ready", ready_event)

	client.run()
	```
	"""

	__slots__ = (
		"http",
		"_events",
		"address",
		"_token",
		"me",
		"connect_websocket",
	)

	def __init__(
			self,
			*,
			address:str,
			token:str,
			connect_websocket: bool = False,
			):
		"""
		Pyskeyを呼び出します。
		呼び出した後、client.run()を使用してログインを行う必要があります。
		"""
		self.http = None
		self._events = {}
		self.address = address
		self._token = token
		self.me = None
		self.connect_websocket = connect_websocket

	async def close_session(self):
		await self.http.close()

	def event(self, func):
		self._events[func.__name__] = func
		return Event(func)

	async def on_ready(self):
		"""
		run()関数を実行後、ログインできたときに発火されます。
		"""
		if self._events.get("on_ready", None) is not None:
			await self._events["on_ready"]()

	def add_event(self, event_name, func: FunctionType):
		"""
		イベントをディスパッチします。
		デコレータを使う方法もあります。
		"""
		self._events[event_name] = func

	def run(self):
		"""
		ログインを試みます。
		"""
		asyncio.run(self.mainloop())

	async def mainloop(self):
		try:
			self.http = aiohttp.ClientSession()
			data = {
				"i": self._token
			}
			async with self.http.post(f"https://{self.address}/api/i", json=data, timeout=aiohttp.ClientTimeout(total=None)) as response:
				self.me = MeDetailed.to_class(await response.json())
			await self.on_ready()
		finally:
			await self.close_session()