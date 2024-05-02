from datetime import datetime
from .user import User
from .object import Object
from .poll import Poll
from .channel import Channel
from .file import File
from dataclasses import dataclass, field
from typing import List

@dataclass
class Note(Object):
    """
    misskeyのノート。
    """

    text: str = ""
    cw: str = ""
    user: User = None
    userId: str = ""
    visibility: str = ""
    replyId: str = ""
    renoteId: str = ""
    reply: "Note" = None
    renote: "Note" = None
    isHidden: bool = False
    mentions: List[str] = field(default_factory=list)
    visibleUserIds: List[str] = field(default_factory=list)
    fileIds: List[str] = field(default_factory=list)
    files: List[File] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    poll: Poll = None
    emojis: List[str] = field(default_factory=list)
    channelId: str = ""
    channel: Channel = None
    localOnly: bool = False
    reactionAcceptance: str = ""
    reactionEmojis: List[str] = field(default_factory=list)
    reactions: List[str] = field(default_factory=list)
    reactionCount: int = 0
    renoteCount: int = 0
    repliesCount: int = 0
    uri: str = ""
    url: str = ""
    reactionAndUserPairCache: List[str] = field(default_factory=list)
    clippedCount: int = 0
    myReaction: str = ""

    def __str__(self):
        return f"{self.userId} : {self.text}"

    def __eq__(self, other):
        return self.id == other.id

    def __post_init__(self):
        if self.createdAt:
            self.createdAt = datetime.strptime(self.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ") if isinstance(self.createdAt, str) else self.createdAt
        if self.user:
            self.user = User.to_class(self.user)
        if self.reply:
            self.reply = Note.to_class(self.reply)
        if self.renote:
            self.renote = Note.to_class(self.renote)
        if self.poll:
            self.poll = Poll.to_class(self.poll)
        if self.channel:
            self.channel = Channel.to_class(self.channel)
        if self.files:
            self.files = [File.to_class(file) for file in self.files]
