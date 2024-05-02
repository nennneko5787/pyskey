from datetime import datetime, timezone
from dataclasses import dataclass

@dataclass
class Achievements():
	"""
	misskeyの実績。
	"""

	name: str
	unlockedAt: datetime

	def __str__(self):
		return f"{self.name}"

	@classmethod
	def to_class(cls, d: dict) -> 'Achievements':
		"""
		辞書からクラスを作成します。
		"""
		return cls(**d)

	def __post_init__(self):
		if self.unlockedAt is not None:
			self.unlockedAt = datetime.strptime(self.unlockedAt, "%Y-%m-%dT%H:%M:%S.%fZ")
