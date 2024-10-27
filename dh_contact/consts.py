"""Константы контактов"""

__author__: str = "Старков Е.П."


from enum import IntEnum


class ContactType(IntEnum):
    """Типы контактов"""

    EMAIL = 1
    PHONE = 2
    TELEGRAM = 3
    VK = 4


# Имена типов контактов
CONTACT_TYPE_NAME = {
    ContactType.EMAIL: "Email",
    ContactType.PHONE: "Телефон",
    ContactType.TELEGRAM: "Telegram",
    ContactType.VK: "VK",
}
