import os
from typing import Optional


def get_value(
    key: str, default: Optional[str] = None, required: bool = True
) -> Optional[str]:
    if value := os.environ.get(key, default=default):
        return value

    if required:
        raise KeyError(f"{key} 변수가 설정돼있지 않습니다.")
