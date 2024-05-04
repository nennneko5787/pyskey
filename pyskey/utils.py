from datetime import datetime, timezone
from typing import Union

class utils():
    @classmethod
    def to_datetime(cls, date: Union[str, int]):
        """
        dateにstrを渡した場合はdatetime.strptime関数で、intを渡した場合はdatetime.fromtimestampを返すユーティリティ関数です。
        """
        try:
            if isinstance(date, str):
                return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
            elif isinstance(date, int):
                return datetime.fromtimestamp((date / 1000), tz=timezone.utc)
            elif isinstance(date, datetime):
                return date
            else:
                raise TypeError("Argument must be a string or an integer")
        except OSError as e:
            if e.errno == 22:
                print(f"Invalid argument: The timestamp is out of range: {date}")
                # 何らかの処理を行うか、エラーを処理する方法を決定する
            else:
                # その他のOSErrorを処理する
                raise