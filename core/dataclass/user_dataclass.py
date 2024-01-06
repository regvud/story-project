from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProfileDataClass:
    id: int
    name: str
    surname: str
    status: str
    age: int
    bio: str
    image: str
    update_at: datetime
    create_at: datetime


@dataclass
class AccountDataClass:
    id: int
    is_writer: bool
    is_premium: bool
    update_at: datetime
    create_at: datetime


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_active: bool
    is_block: bool
    is_staff: bool
    is_superuser: bool
    update_at: datetime
    create_at: datetime
    profile: ProfileDataClass
    account: AccountDataClass
