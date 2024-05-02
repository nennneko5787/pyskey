from dataclasses import dataclass

@dataclass
class Role():
	"""
	misskeyのロール。
	"""

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
