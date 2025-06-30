from pydantic import BaseModel
from typing import Optional

class NotificationPreferenceCreate(BaseModel):
    category: str
    keyword: Optional[str]

class NotificationPrefrenceUpdate(NotificationPreferenceCreate):
    is_enabled: bool

class NotificationPreferenceOut(NotificationPreferenceCreate):
    id: int
    user_id: int
