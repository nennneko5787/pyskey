from datetime import datetime
from dataclasses import dataclass

@dataclass
class Object:
    """
    Pyskeyでのオブジェクトの基底クラス。
    """

    createdAt: datetime
    id: str

    @classmethod
    def to_class(cls, d: dict) -> 'Object':
        """
        辞書からクラスを作成します。
        """
        return cls(**d)
