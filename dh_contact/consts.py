"""Константы контактов"""

__author__: str = 'Старков Е.П.'


from enum import IntEnum


class ContactType(IntEnum):
    """Типы контактов"""
    EMAIL: int = 1
    PHONE: int = 2
    TELEGRAM: int = 3
    VK: int = 4


# Имена типов контактов
CONTACT_TYPE_NAME = {
    ContactType.EMAIL: 'Email',
    ContactType.PHONE: 'Телефон',
    ContactType.TELEGRAM: 'Telegram',
    ContactType.VK: 'VK'
}
