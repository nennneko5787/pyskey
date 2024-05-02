from datetime import datetime, timezone
from .object import Object
from .avatarDecoration import AvatarDecoration
from .badgeRole import BadgeRole
from typing import List, Optional, Union
from dataclasses import dataclass, field

@dataclass
class Emojis:
    # You can define specific fields as needed
    pass

@dataclass
class User(Object):
	"""
	misskeyのユーザー。
	"""

	name: Optional[str] = None
	username: str = None
	host: Optional[str] = None
	avatarUrl: Optional[str] = None
	avatarBlurhash: Optional[str] = None
	avatarDecorations: List[AvatarDecoration] = None
	emojis: Emojis = None
	onlineStatus: str = None
	badgeRoles: List[BadgeRole] = None
	isBot: bool = None
	isCat: bool = None

	def __str__(self):
		return f"{self.name} ({self.username})"

	def __eq__(self, other):
		return self.id == other.id

	def __post_init__(self):
		if self.createdAt is not None:
			self.createdAt = datetime.strptime(self.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ")
		if len(self.avatarDecorations) != 0:
			self.avatarDecorations = [AvatarDecoration.to_class(avatarDecoration) for avatarDecoration in self.avatarDecorations]
		if len(self.badgeRoles) != 0:
			self.badgeRoles = [BadgeRole.to_class(badgeRole) for badgeRole in self.badgeRoles]