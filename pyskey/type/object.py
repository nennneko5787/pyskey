from datetime import datetime
from typing import List, Optional, Union
from dataclasses import dataclass

@dataclass
class Object:
    """
    Pyskeyでのオブジェクトの基底クラス。
    """

    createdAt: Optional[datetime] = None
    id: str = None

    @classmethod
    def to_class(cls, d: dict) -> 'Object':
        """
        辞書からクラスを作成します。
        """
        return cls(**d)
