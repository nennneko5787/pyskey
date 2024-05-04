from datetime import datetime, timezone
from .object import Object
from .user import User
from ..utils import utils
from dataclasses import dataclass

@dataclass
class FileProperty():
    """
    ファイルのプロパティ。
    """
    width: int
    height: int
    orientation: int
    avgColor: str
    
    @classmethod
    def to_class(cls, d: dict) -> 'FileProperty':
        """
        辞書からクラスを作成します。
        """
        return cls(**d)


@dataclass
class File(Object):
    """
    misskeyのファイル。
    """
    name: str = ""
    type: str = ""
    md5: str = ""
    size: int = 0
    isSensitive: int = 0
    blurhash: str = ""
    properties: FileProperty = None
    url: str = ""
    thumbnailUrl: str = ""
    comment: str = ""
    folderId: str = ""
    userId: str = ""
    user: User = None

    def __eq__(self, other):
        return self.id == other.id

    def __post_init__(self):
        if self.createdAt is not None:
            self.createdAt = utils.to_datetime(self.createdAt)
        if self.properties is not None:
            self.properties = FileProperty.to_class(self.properties)
        if self.user is not None:
            self.user = User.to_class(self.user)