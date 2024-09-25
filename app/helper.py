from enum import Enum
import httpx
from fastapi import status, HTTPException
from httpx import URL, _types
from typing import Mapping


class Tags(Enum):
    home = "home"
    qna = "qna"
    auth = "auth"
    analytics = "analytics"



