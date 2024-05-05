import asyncio
from .http import HTTP
from .type.medetailed import MeDetailed
from .type.note import Note
from .type.enums import *
from .type.errors import *
from .type.poll import Poll
from types import FunctionType
from typing import Optional, Type
from types import TracebackType

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
	.. code-block:: python3
	
		client = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")

	クラスを継承する方法でも呼び出せるかもしれません。(未検証)

	イベントを追加するには、デコレータを使用するか、add_event関数を使用します。
	.. code-block:: python3

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
	"""

	__slots__ = (
		"_events",
		"me",
		"address",
		"token",
		"http",
		"connect_websocket",
		"is_closed",
	)

	def __init__(
			self,
			*,
			address:str,
			token:str,
			connect_websocket: bool = False,
			):
		"""
		Pyskeyを初期化します。
		初期化した後、Client.run()関数を実行する必要があります。

   		Parameters
		----------
		address : str
			misskeyインスタンスのアドレス。
		token : str
			misskeyアカウントのトークン。漏出しないように気を付けてください。
		connect_websocket : bool = False
			WebSocketに接続するかどうか。

		Returns
		-------
		Client
			初期化したClientのインスタンス。
		"""
		self._events = {}
		self.address = address
		self.token = token
		self.http = None
		self.me = None
		self.connect_websocket = connect_websocket
		self.is_closed = False

	async def __aenter__(self):
		return self

	async def __aexit__(
		self,
		exc_type: Optional[Type[BaseException]],
		exc_value: Optional[BaseException],
		traceback: Optional[TracebackType],
	) -> None:
		if not self.is_closed:
			await self.close()

	def event(self, func):
		self._events[func.__name__] = func
		return Event(func)

	async def on_ready(self):
		"""
		run()関数を実行後、ログインできたときに発火されます。
		"""
		if self._events.get("on_ready", None) is not None:
			await self._events["on_ready"]()

	def add_event(self, event_name: str, func: FunctionType):
		"""
		イベントを登録します。
		この関数を使う方法のほかに、デコレータを利用してイベントを登録する方法もあります。

   		Parameters
		----------
		event_name : str
			登録するイベントの名前。間違っていてもエラーは出ません。
		func : FunctionType
			イベントが実行される関数。
		"""
		self._events[event_name] = func

	async def close(self):
		"""
		初期化したPyskeyをクローズします。
		プログラムの途中でこの関数を呼ぶのはお勧めしません。
		"""
		
		self.is_closed = True
		await self.http.close()

	def run(self):
		"""
		ログインを試みます。
		"""

		async def runner():
			async with self:
				await self.start()

		asyncio.run(runner())

	async def start(self):
		try:
			self.http = HTTP(
				address=self.address,
				token=self.token,
			)

			response, code = await self.http.post(f"https://{self.address}/api/i")
			if code == 200:
				response.setdefault("_client", self)
				self.me = MeDetailed.to_class(response)
				await self.on_ready()
			elif code == 401:
				raise UserNotAuthorizedError("Login failed. Incorrect token.")
			elif code == 403:
				raise AuthorizeForbiddenError()
			elif code == 404:
				raise UserNotAuthorizedError()
		finally:
			await self.close()

	# ここからはmisskey関係の関数
 
	async def create_note(
		self,
		text: str,
		*,
		visibility: NoteVisibility = NoteVisibility.public,
		visibleUserIds: list = None,
		cw: str = None,
		localOnly: bool = False,
		reactionAcceptance: ReactionAcceptance = ReactionAcceptance.all,
		noExtractMentions: bool = False,
		noExtractHashtags: bool = False,
		noExtractEmojis: bool = False,
		replyId: str = None,
		renoteId: str = None,
		fileIds: list = None,
		mediaIds: list = None,
		poll: Poll = None,
	) -> Note:

		"""
		ノートを作成します。

   		Parameters
		----------
		text : str
			ノートの本文。
		visibility : NoteVisibility = NoteVisibility.public
			ノートの公開範囲。
		visibleUserIds : list = None
			ノートを公開するユーザーのリスト。
			visibilityをNoteVisibility.specifiedにしたときに指定します。
		cw : str = None
			ノートの注訳。
			これをNone以外に指定した場合、ノートが閲覧注意になります。
		localOnly : str = False
			ノートを連合しないかどうか。
		reactionAcceptance : ReactionAcceptance = ReactionAcceptance.all
			リアクションの許可範囲。
		noExtractMentions : bool = False
			メンションを展開するかどうか。
		noExtractHashtags : bool = False
			ハッシュタグを展開するかどうか。
		noExtractEmojis : bool = False
			絵文字を展開するかどうか。
		replyId : str = None
			返信先ノートのID。
			Note.reply_note関数で代用できます。
		renoteId : str = None
			リノート先ノートのID。
			Note.renote_note関数で代用できます。
			また、これを指定した場合、textを""(空欄)にするとただのリノートになります。
			それ以外の場合は引用リノートになります。
		fileIds : list = None
			添付ファイルのIDのリスト。
		mediaIds : list = None
			添付メディアファイルのIDのリスト。
		poll : Poll = None
			アンケート。
			以下のようにして作成します。
			.. code-block:: python3

				poll = pyskey.Poll(
					choices=["選択肢1", "選択肢2", "選択肢3"]
				)
				await misskey.create_note(
					"アンケートのテスト",
					poll=poll,
				)
			
		Returns
		-------
		Note
			作成したNoteのインスタンス。
		"""

		data = {
			"text": text,
			"visibility": visibility,
			"cw": cw,
			"localOnly": localOnly,
			"reactionAcceptance": reactionAcceptance,
			"noExtractMentions": noExtractMentions,
			"noExtractHashtags": noExtractHashtags,
			"noExtractEmojis": noExtractEmojis,
			"replyId": replyId,
			"renoteId": renoteId,
		}

		if visibleUserIds is not None:
			data.setdefault("visibleUserIds", visibleUserIds)
		if fileIds is not None:
			data.setdefault("fileIds", fileIds)
		if mediaIds is not None:
			data.setdefault("mediaIds", mediaIds)
		if poll is not None:
			data.setdefault("poll", poll.to_dict())
		print(data)

		response, code = await self.http.post(
			f"https://{self.address}/api/notes/create",
			data=data
		)

		if code == 200:
			response["createdNote"].setdefault("_client", self)
			return Note.to_class(response["createdNote"])
		elif code == 400:
			raise ClientError(response)
		elif code == 401:
			raise UserNotAuthorizedError()
		elif code == 429:
			raise RateLimitedError()
