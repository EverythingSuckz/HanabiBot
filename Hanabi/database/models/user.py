from typing import List, Optional
from datetime import datetime

import ormar

from .model import BaseMeta

class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: int = ormar.BigInteger(primary_key=True)
    full_name: Optional[str] = ormar.String(max_length=500, nullable=True)
    username: Optional[str] = ormar.String(max_length=500, nullable=True)
    started_date: datetime = ormar.DateTime(default=datetime.utcnow)

    async def add_or_update_user(self, user_id: int, full_name: str, username: Optional[str]) -> None:
        user, _ = await self.objects.get_or_create(id=user_id, _defaults={"full_name": full_name, "username": username})
        user.full_name = full_name
        user.username = username
        await user.update()

    async def get_user_by_username(self, username: str) -> Optional["User"]:
        return await User.objects.get_or_none(username=username.strip("@ "))
 

    async def get_all_users(self) -> List["User"]:
        return await User.objects.all()


    async def get_total_user_count(self) -> int:
        return await User.objects.count()