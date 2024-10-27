"""Схемы данных для работы с контактами"""

from pydantic import BaseModel


class ContactRegisterData(BaseModel):
    """Контакты при регистрации"""

    email: str
    phone: str | None


class ContactPublicData(BaseModel):
    """Публичные данные контакта"""

    value: str
    human_read_type: str
