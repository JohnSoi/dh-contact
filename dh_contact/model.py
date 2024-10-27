"""Модуль работы с моделью контактов"""

__author__: str = 'Старков Е.П.'

from sqlalchemy import String, SmallInteger, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dh_base.columns import IdColumns
from dh_base.mixins import ConvertToDictMixin
from .consts import CONTACT_TYPE_NAME
from dh_base.database import Base


class ContactModel(IdColumns, Base, ConvertToDictMixin):
    """Модель контактов"""
    __tablename__: str = 'contacts'

    value: Mapped[str] = mapped_column(String(60), index=True)
    type: Mapped[int] = mapped_column(SmallInteger)
    is_confirm: Mapped[bool] = mapped_column(Boolean, default=False)
    is_main: Mapped[bool] = mapped_column(Boolean, default=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped['UserModel'] = relationship(back_populates='contacts', lazy=False)

    def human_read_type(self) -> str:
        """Человекочитаемый тип контакта"""
        return CONTACT_TYPE_NAME[self.type]
