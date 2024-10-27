"""Исключения контактов"""

__author__: str = "Старков Е.П."


from fastapi import status
from dh_base.exceptions import BaseAppException


class EmailExist(BaseAppException):
    """Почта уже существует"""

    STATUS_CODE: int = status.HTTP_409_CONFLICT
    DETAIL: str | None = "Данный email уже используется в системе"


class PhoneExist(BaseAppException):
    """Телефон уже существует"""

    STATUS_CODE: int = status.HTTP_409_CONFLICT
    DETAIL: str | None = "Данный телефон уже используется в системе"


class NotMainContact(BaseAppException):
    """Только один основной контакт типа"""

    STATUS_CODE: int = status.HTTP_400_BAD_REQUEST
    DETAIL: str | None = "Должен быть хотя бы один основной контакт"


class HaveContact(BaseAppException):
    """Нет основного контакт типа"""

    STATUS_CODE: int = status.HTTP_400_BAD_REQUEST
    DETAIL: str | None = "Может быть только один основной контакт"
