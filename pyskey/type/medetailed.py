from datetime import datetime, timezone
from typing import Any
from .object import Object
from .role import Role
from .note import Note
from .avatarDecoration import AvatarDecoration
from .badgeRole import BadgeRole
from .achievement import Achievement
from ..utils import utils
from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class MeDetailed(Object):
    """
    自分の情報。
    内部的には /api/i から取得します。
    """

    _client: Any = None
    name: str = ""
    username: str = ""
    host: str = ""
    avatarUrl: str = ""
    avatarBlurhash: str = ""
    avatarDecorations: List[AvatarDecoration] = field(default_factory=list)  # Use default_factory for lists
    isBot: bool = False
    isCat: bool = False
    emojis: Dict[str, str] = field(default_factory=dict)
    onlineStatus: str = ""
    badgeRoles: List[BadgeRole] = field(default_factory=list)
    url: str = ""
    uri: str = ""
    movedTo: str = ""
    alsoKnownAs: str = ""
    updatedAt: datetime = datetime.now(timezone.utc)
    lastFetchedAt: datetime = datetime.now(timezone.utc)
    bannerUrl: str = ""
    bannerBlurhash: str = ""
    isLocked: bool = False
    isSilenced: bool = False
    isLimited: bool = False
    isSuspended: bool = False
    description: str = ""
    location: str = ""
    birthday: datetime = datetime.now(timezone.utc)
    lang: str = ""
    fields: List[str] = field(default_factory=list)
    verifiedLinks: List[str] = field(default_factory=list)
    followersCount: int = 0
    followingCount: int = 0
    notesCount: int = 0
    pinnedNoteIds: List[str] = field(default_factory=list)
    pinnedNotes: List[Note] = field(default_factory=list)
    pinnedPageId: str = ""
    pinnedPage: List[str] = field(default_factory=list)
    publicReactions: bool = False
    followersVisibility: str = ""
    followingVisibility: str = ""
    twoFactorEnabled: bool = False
    usePasswordLessLogin: bool = False
    securityKeys: bool = False
    roles: List[Role] = field(default_factory=list)
    memo: str = ""
    avatarId: str = ""
    bannerId: str = ""
    isModerator: bool = False
    isAdmin: bool = False
    injectFeaturedNote: bool = False
    receiveAnnouncementEmail: bool = False
    alwaysMarkNsfw: bool = False
    autoSensitive: bool = False
    carefulBot: bool = False
    autoAcceptFollowed: bool = False
    noCrawle: bool = False
    preventAiLearning: bool = False
    isExplorable: bool = False
    isDeleted: bool = False
    twoFactorBackupCodesStock: str = ""
    hideOnlineStatus: bool = False
    hasUnreadSpecifiedNotes: bool = False
    hasUnreadMentions: bool = False
    hasUnreadAnnouncement: bool = False
    unreadAnnouncements: List[str] = field(default_factory=list)
    hasUnreadAntenna: bool = False
    hasUnreadChannel: bool = False
    hasUnreadNotification: bool = False
    hasPendingReceivedFollowRequest: bool = False
    unreadNotificationsCount: int = 0
    hardMutedWords: List[str] = field(default_factory=list)
    mutedWords: List[str] = field(default_factory=list)
    mutedInstances: List[str] = field(default_factory=list)
    mutingNotificationTypes: List[str] = field(default_factory=list)
    notificationRecieveConfig: Dict[str, str] = field(default_factory=dict)
    emailNotificationTypes: List[str] = field(default_factory=list)
    achievements: List[Achievement] = field(default_factory=list)
    loggedInDays: int = 0
    policies: Dict[str, str] = field(default_factory=dict)

    def __str__(self):
        return f"{self.name} ({self.username})"

    def __eq__(self, other):
        return self.id == other.id

    def __post_init__(self):
        if self.roles:
            self.roles.setdefault("_client", self._client)
            self.roles = [Role.to_class(role) for role in self.roles]
        if self.pinnedNotes:
            self.pinnedNotes.setdefault("_client", self._client)
            self.pinnedNotes = [Note.to_class(note) for note in self.pinnedNotes]
        if self.avatarDecorations:
            self.avatarDecorations = [AvatarDecoration.to_class(avatarDecoration) for avatarDecoration in self.avatarDecorations]
        if self.badgeRoles:
            self.badgeRoles = [BadgeRole.to_class(badgeRole) for badgeRole in self.badgeRoles]
        if self.achievements:
            self.achievements = [Achievement.to_class(achievements) for achievements in self.achievements]
