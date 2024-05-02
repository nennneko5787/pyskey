from dataclasses import dataclass, field

@dataclass
class AvatarDecoration:
    id: str = ""
    angle: float = 0.0
    flipH: bool = False
    url: str = ""
    offsetX: float = 0.0
    offsetY: float = 0.0

    @classmethod
    def to_class(cls, d: dict) -> 'AvatarDecoration':
        """
        辞書からクラスを作成します。
        """
        return cls(**d)
