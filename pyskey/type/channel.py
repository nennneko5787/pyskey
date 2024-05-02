from dataclasses import dataclass

@dataclass
class Channel():
	id: str
	name: str
	color: str
	isSensitive: bool
	allowRenoteToExternal: bool
	userId: str

	@classmethod
	def to_class(cls, d: dict) -> 'Channel':
		"""
		辞書からクラスを作成します。
		"""
		return cls(**d)