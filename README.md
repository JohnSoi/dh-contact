# Подсистема контактов DH

---

## Описание 

Базовые механизмы работы с контактами в приложениях экосистемы DH

---

## Состав

* ```consts``` - константы
  * ```ContactType``` - типы контактов
  * ```CONTACT_TYPE_NAME``` - карта типов и названий
* ```exceptions``` - исключения
* ```models``` - модели
* ```repository``` - репозитории для работы с данными
* ```schemas``` - схемы данных
---

## Подключение

Для подключения используется команда:
```bash
poetry add git+https://github.com/JohnSoi/dh-contact.git
```

В файл ```migrations/env.py``` нужно добавить импорт моделей:
```python
from dh_contact.model import *
```

В файле ```.env``` должны быть следующие поля:

```dotenv
SECRET_KEY=
CRYPTO_CONTEXT_SCHEME=
ENCODE_ALGORITHM=
TOKEN_EXPIRE_DAY=
TOKEN_COOKIE_NAME=
CELERY_AUTH_NAME=
```