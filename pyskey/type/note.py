from datetime import datetime, timezone
from .user import User
from .object import Object
from dataclasses import dataclass

@dataclass
class Note(Object):
	"""
	misskeyのノート。
	"""

	text: str
	cw: str
	user: User
	userId: str
	visibility: str

	def __post_init__(self):
		if self.createdAt is not None:
			self.createdAt = datetime.strptime(self.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ")
		if self.user is not None:
			self.user = User.to_class(self.user)
