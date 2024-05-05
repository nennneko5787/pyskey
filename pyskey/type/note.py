from datetime import datetime
from typing import Any
from .user import User
from .object import Object
from .poll import Poll
from .channel import Channel
from .file import File
from .errors import *
from .enums import *
from dataclasses import dataclass, field
from typing import List

@dataclass
class Note(Object):
	"""
	misskeyのノート。
	"""

	_client: Any = None
	text: str = ""
	cw: str = ""
	user: User = None
	userId: str = ""
	visibility: str = ""
	replyId: str = ""
	renoteId: str = ""
	reply: "Note" = None
	renote: "Note" = None
	isHidden: bool = False
	mentions: List[str] = field(default_factory=list)
	visibleUserIds: List[str] = field(default_factory=list)
	fileIds: List[str] = field(default_factory=list)
	files: List[File] = field(default_factory=list)
	tags: List[str] = field(default_factory=list)
	poll: Poll = None
	emojis: List[str] = field(default_factory=list)
	channelId: str = ""
	channel: Channel = None
	localOnly: bool = False
	reactionAcceptance: str = ""
	reactionEmojis: List[str] = field(default_factory=list)
	reactions: dict[str] = field(default_factory=dict)
	reactionCount: int = 0
	renoteCount: int = 0
	repliesCount: int = 0
	uri: str = ""
	url: str = ""
	reactionAndUserPairCache: List[str] = field(default_factory=list)
	clippedCount: int = 0
	myReaction: str = ""

	async def reply_note(
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
		fileIds: list = None,
		mediaIds: list = None,
		poll: Poll = None,
	) -> 'Note':
		"""
		ノートにリプライします。

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
		
		return await self._client.create_note(
			text=text,
			visibility=visibility,
			visibleUserIds=visibleUserIds,
			cw=cw,
			localOnly=localOnly,
			reactionAcceptance=reactionAcceptance,
			noExtractMentions=noExtractMentions,
			noExtractHashtags=noExtractHashtags,
			noExtractEmojis=noExtractEmojis,
			replyId=self.id,
			fileIds=fileIds,
			mediaIds=mediaIds,
			poll=poll,
		)
	
	async def renote_note(
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
		fileIds: list = None,
		mediaIds: list = None,
		poll: Poll = None,
	) -> 'Note':
		"""
		ノートをリノート・引用リノートします。

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

		return await self._client.create_note(
			text=text,
			visibility=visibility,
			visibleUserIds=visibleUserIds,
			cw=cw,
			localOnly=localOnly,
			reactionAcceptance=reactionAcceptance,
			noExtractMentions=noExtractMentions,
			noExtractHashtags=noExtractHashtags,
			noExtractEmojis=noExtractEmojis,
			renoteId=self.id,
			fileIds=fileIds,
			mediaIds=mediaIds,
			poll=poll,
		)

	async def add_reaction(self, reaction: str) -> 'Note':
		"""
		ノートにリアクションを追加します。

   		Parameters
		----------
		reaction : str
			リアクションのID。
			
		Returns
		-------
		Note
			変更後のNoteのインスタンス。
		"""

		data = {
			"noteId": self.id,
			"reaction": reaction
		}

		response, code = await self._client.http.post(
			f"https://{self._client.address}/api/notes/reactions/create",
			data=data
		)

		if code == 204:
			self.reactions[reaction] = self.reactions.get(reaction, 0) + 1
			return self
		elif code == 400:
			raise ClientError(response)
		elif code == 401:
			raise UserNotAuthorizedError()
		elif code == 429:
			raise RateLimitedError()

	async def delete_reaction(self, reaction: str) -> 'Note':
		"""
		ユーザーがつけたリアクションをノートから削除します。
			
		Returns
		-------
		Note
			変更後のNoteのインスタンス。
		"""

		data = {
			"noteId": self.id
		}

		response, code = await self.http.post(
			f"https://{self.address}/api/notes/reactions/create",
			data=data
		)

		if code == 204:
			self.reactions[reaction] = self.reactions.get(reaction, 0) - 1
			return self
		elif code == 400:
			raise ClientError(response)
		elif code == 401:
			raise UserNotAuthorizedError()
		elif code == 429:
			raise RateLimitedError()

	def __str__(self):
		return f"{self.userId} : {self.text}"

	def __eq__(self, other):
		return self.id == other.id

	def __post_init__(self):
		if self.createdAt:
			self.createdAt = datetime.strptime(self.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ") if isinstance(self.createdAt, str) else self.createdAt
		if self.user:
			self.user.setdefault("_client", self._client)
			self.user = User.to_class(self.user)
		if self.reply:
			self.reply.setdefault("_client", self._client)
			self.reply = Note.to_class(self.reply)
		if self.renote:
			self.renote.setdefault("_client", self._client)
			self.renote = Note.to_class(self.renote)
		if self.poll:
			self.poll = Poll.to_class(self.poll)
		if self.channel:
			self.channel = Channel.to_class(self.channel)
		if self.files:
			self.files = [File.to_class(file) for file in self.files]
