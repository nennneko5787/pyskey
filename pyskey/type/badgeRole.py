from dataclasses import dataclass, field

@dataclass
class BadgeRole:
    name: str = ""
    iconUrl: str = ""
    displayOrder: int = 0
    behavior: str = ""

    @classmethod
    def to_class(cls, d: dict) -> 'BadgeRole':
        """
        辞書からクラスを作成します。
        """
        return cls(**d)