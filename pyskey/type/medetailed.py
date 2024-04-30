from datetime import datetime, timezone
from .object import Object
from .role import Role
from dataclasses import dataclass

@dataclass
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
    movedTo: str
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
    pinnedNotes: list
    pinnedPageId: str
    pinnedPage: list
    publicReactions: bool
    followersVisibility: str
    followingVisibility: str
    twoFactorEnabled: bool
    usePasswordLessLogin: bool
    securityKeys: bool
    roles: list
    memo: str
    avatarId: str
    bannerId: str
    isModerator: bool
    isAdmin: bool
    injectFeaturedNote: bool
    receiveAnnouncementEmail: bool
    alwaysMarkNsfw: bool
    autoSensitive: bool
    carefulBot: bool
    autoAcceptFollowed: bool
    noCrawle: bool
    preventAiLearning: bool
    isExplorable: bool
    isDeleted: bool
    twoFactorBackupCodesStock: str
    hideOnlineStatus: bool
    hasUnreadSpecifiedNotes: bool
    hasUnreadMentions: bool
    hasUnreadAnnouncement: bool
    unreadAnnouncements: list
    hasUnreadAntenna: bool
    hasUnreadChannel: bool
    hasUnreadNotification: bool
    hasPendingReceivedFollowRequest: bool
    unreadNotificationsCount: int
    mutedWords: list
    mutedInstances: list
    mutingNotificationTypes: list
    notificationRecieveConfig: dict
    emailNotificationTypes: list
    achievements: list
    loggedInDays: int
    policies: dict

    def __post_init__(self):
        if self.createdAt is not None:
            self.createdAt = datetime.strptime(self.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        if self.updatedAt is not None:
            self.updatedAt = datetime.strptime(self.updatedAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        if self.lastFetchedAt is not None:
            self.lastFetchedAt = datetime.strptime(self.lastFetchedAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        if self.birthday is not None:
            self.birthday = datetime.strptime(self.birthday, "%Y-%m-%d")
