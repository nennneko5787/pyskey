from dataclasses import dataclass
from typing import Any

@dataclass
class Role():
	"""
	misskeyのロール。
	"""

	_client: Any
	id: str
	name: str
	color: str
	iconUrl: str
	description: str
	isModerator: bool
	isAdministrator: bool
	displayOrder: int

	def __eq__(self, other):
		return self.id == other.id

	@classmethod
	def to_class(cls, d: dict) -> 'Role':
		"""
		辞書からクラスを作成します。
		"""
		return cls(**d)
