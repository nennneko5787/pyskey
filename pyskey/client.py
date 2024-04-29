import asyncio
import aiohttp

class Event:
	def __init__(self, func):
		self.func = func

	def __get__(self, instance, owner):
		return self if instance is None else self.wrapper(instance)

	def wrapper(self, instance):
		async def wrapped(*args, **kwargs):
			return await self.func(instance)
		return wrapped

class Client:
	"""
	Pyskeyのクライアントクラス。
	以下の方法で呼び出すことを推奨します。
	```
	client = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")
	```
	クラスを継承する方法でも呼び出せるかもしれません。(未検証)

	イベントを追加するには、dispatch_event関数を使用します。
	```
	client = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")

	# デコレータを使用する方法
	@client.event
	async def on_ready():
		print(f"{client.user.address}")
	```
	"""

	def __init__(
			self,
			*,
			address:str,
			token:str,
			):
		"""
		Pyskeyを呼び出します。
		呼び出した後、client.run()を使用してログインを行う必要があります。
		"""
		self.http = None
		self.events = {}
		self.address = address
		self.token = token

	async def close_session(self):
		await self.http.close()

	def event(self, func):
		self.events[func.__name__] = func
		return Event(func)

	def dispatch_event(self, event_name, *args, **kwargs):
		"""
		イベントをディスパッチします。
		デコレータを使う方法もあります。
		"""
		if event_name in self.events:
			return self.events[event_name]()

	def run(self):
		"""
		ログインを試みます。
		"""
		asyncio.run(self.mainloop())

	async def mainloop(self):
		try:
			self.http = aiohttp.ClientSession()
			data = {
				"i": self.token
			}
			async with self.http.post(f"https://{self.address}/api/i", json=data, timeout=aiohttp.ClientTimeout(total=None)) as response:
				print(await response.json())
		finally:
			await self.close_session()