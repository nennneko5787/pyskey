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
