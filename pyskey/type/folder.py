from datetime import datetime, timezone
from .object import Object
from dataclasses import dataclass

@dataclass
class Folder(Object):
    """
    misskeyのフォルダ。
    """

    name: str = ""
    parentId: str = ""
    foldersCount: int = 0
    filesCount: int = 0
    parent: "Folder" = None

    def __post_init__(self):
        if self.createdAt is not None:
            self.createdAt = datetime.strptime(self.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        if self.parent is not None:
            self.parent = Folder.to_class(self.parent)