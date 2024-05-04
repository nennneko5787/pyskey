from datetime import datetime, timezone
from ..utils import utils
from typing import List, Union
from dataclasses import dataclass, field

@dataclass
class PollChoices:
	text: str
	isVoted: bool = False
	votes: int = 0

	def to_dict(self):
		return self.__dict__

	@classmethod
	def to_class(cls, d: dict) -> 'PollChoices':
		"""
		辞書からクラスを作成します。
		"""
		return cls(**d)

@dataclass
class Poll():
	"""
	misskeyの投票。
	"""

	expiresAt: datetime = None
	multiple: bool = False
	choices: List[Union[PollChoices, str]] = field(default_factory=list)

	@classmethod
	def to_class(cls, d: dict) -> 'Poll':
		"""
		辞書からクラスを作成します。
		"""
		return cls(**d)
	
	def to_dict(self):
		poll = self.__dict__
		if poll["expiresAt"] is not None:
			poll["expiresAt"] = self.expiresAt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
		choices = []
		for choice in self.choices:
			if isinstance(choice, PollChoices):
				choices.append(choice.to_dict())
			else:
				choices.append(str(choice))
		poll["choices"] = choices
		return poll

	def __post_init__(self):
		if self.expiresAt is not None:
			self.expiresAt = utils.to_datetime(self.expiresAt)
		if self.choices is not None:
			new_choices = []
			for choice in self.choices:
				if isinstance(choice, PollChoices):
					new_choices.append(PollChoices.to_class(choice))
				else:
					new_choices.append(str(choice))
			self.choices = new_choices
