from datetime import datetime, timezone
from .note import Note
from .object import Object
from dataclasses import dataclass

@dataclass
class User(Object):
	"""
	misskeyのユーザー。
	"""

	username: str
	host: str
	name: str
	onlineStatus: str
	avatarUrl: str
	avatarBlurhash: str

	def __post_init__(self):
		if self.createdAt is not None:
			self.createdAt = datetime.strptime(self.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ")
