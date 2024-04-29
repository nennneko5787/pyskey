from datetime import datetime, timezone
from .object import Object

class MeDetailed(Object):
    """
    自分の情報。
    内部的には /api/i から取得します。
    """

    name: str
    username: str
    host: str
    avatarUrl: str
    avatarBlurhash: str
    avatarDecorations: list
    isBot: bool
    isCat: bool
    emojis: dict
    onlineStatus: str
    badgeRoles: list
    url: str
    uri: str
    moveTo: str
    alsoKnownAs: str
    updatedAt: datetime
    lastFetchedAt: datetime
    bannerUrl: str
    bannerBlurhash: str
    isLocked: bool
    isSilenced: bool
    isLimited: bool
    isSuspended: bool
    description: bool
    location: str
    birthday: datetime
    lang: str
    fields: list
    verifiedLinks: list
    followersCount: int
    followingCount: int
    notesCount: 292
    pinnedNoteIds: list
    pinnedNotes: list[Note]

    def __post_init__(self):
        super().__post_init__()
        # datetime に変換
        self.createdAt = datetime.strptime(self.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.updatedAt = datetime.strptime(self.updatedAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.lastFetchedAt = datetime.strptime(self.lastFetchedAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.birthday = datetime.strptime(self.birthday, "%Y-%m-%d")
