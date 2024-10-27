"""Репозиторий контактов"""

__author__: str = 'Старков Е.П.'


from typing import Type, Any

from pydantic import EmailStr

from dh_base.repositories import BaseRepository
from .consts import ContactType
from .exceptions import NotMainContact, HaveContact, EmailExist, PhoneExist
from .model import ContactModel


class ContactRepository(BaseRepository):
    """Репозиторий контактов"""
    @property
    def model(self) -> Type[ContactModel]:
        return ContactModel

    @property
    def ordering_field_name(self) -> str:
        return ContactModel.__table__.c.type

    @staticmethod
    async def _before_update(entity: ContactModel, new_entity_data: dict[str, Any]) -> None:
        if 'is_main' not in new_entity_data or entity.is_main == new_entity_data.get('is_main'):
            return

        main_contact: ContactModel = await ContactRepository().find_one_or_none(
            type=entity.type, user_id=entity.user_id, is_main=True
        )

        if not new_entity_data.get('is_main') and not main_contact:
            raise NotMainContact()

        if new_entity_data.get('is_main') and main_contact:
            raise HaveContact()

    async def check_email_exist(self, email: EmailStr) -> None:
        """
        Проверка на существование почты. Если существует - исключение

        @param email: почта
        """
        email_exist: bool = await self.find_one_or_none(
            value=email, type=ContactType.EMAIL
        ) is not None

        if email_exist:
            raise EmailExist()

    async def check_phone_exist(self, phone: str) -> None:
        """
        Проверка на существование телефона. Если существует - исключение

        @param phone: телефон
        """
        phone_exist: bool = \
            await self.find_one_or_none(
                value=phone, type=ContactType.PHONE
            ) is not None

        if phone_exist:
            raise PhoneExist()
