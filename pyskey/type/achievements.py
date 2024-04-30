from datetime import datetime, timezone
from dataclasses import dataclass

@dataclass
class Achievements():
	"""
	misskeyの実績。
	"""

	name: str
	unlockedAt: datetime

	def __post_init__(self):
		if self.unlockedAt is not None:
			self.unlockedAt = datetime.strptime(self.unlockedAt, "%Y-%m-%dT%H:%M:%S.%fZ")
