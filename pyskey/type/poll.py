from datetime import datetime, timezone
from dataclasses import dataclass

@dataclass
class PollChoices:
	isVoted: bool
	text: str
	votes: int

@dataclass
class Poll():
	"""
	misskeyの投票。
	"""

	expiresAt: datetime
	multiple: bool
	choices: PollChoices

	@classmethod
	def to_class(cls, d: dict) -> 'Poll':
		"""
		辞書からクラスを作成します。
		"""
		return cls(**d)

	def __post_init__(self):
		if self.expiresAt is not None:
			self.expiresAt = datetime.strptime(self.expiresAt, "%Y-%m-%dT%H:%M:%S.%fZ")
