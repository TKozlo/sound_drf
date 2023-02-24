Sound 

Проект Sound - это аудио платформа, которая позволяет людям находить, слушать и скачивать музыку. Музыканты могут загружать музыку для бесплатного использования. Можно преобразовать как платформу для самостоятельного изучения иностранного языка.

Функционал
    Авторизация через Google
    Редактирование профиля пользователя
    Создать, редактировать и удалять:
        Альбомы
        Плейлисты
        Треки
        Лицензии
    Загрузка, воспроизведение и скачивание музальных файлов
    Добавление исполнителя в избранное
    Комментарии к треку

Присутствует валидатор для загружаемых файлов, аутентификация пользователя с использованием JWT


Инструменты

    Python >= 3.10
    Django Rest Framework


Что нужно перед стартом:
1) в sound/settings.py изменяем на свои параметры
# Base
DEBUG=0
SECRET_KEY= твойСекретныйКлюч
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# Google client
GOOGLE_CLIENT_ID='твой_Гугл_клиент_айди'
GOOGLE_SECRET_KEY='твой_Гугл_секретный_ключ'

По дефолту БД на sqlite3, но по желанию можно postgres. Ниже приведены нужные поля для заполнения( и лишний раз проконтролируй себя с официальной документацией). 

# Data Base
POSTGRES_DB=имя_твоей_бд
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_USER=имя_твоего_пользователя
POSTGRES_PASSWORD=пароль_бд
POSTGRES_HOST=db
POSTGRES_PORT=5432


Если параноик и хотите заморочиться, то в корне проекта создать .env и прописать свои настройки. Но не забудьте установить перед эти django-environ и следовать инструкциям из документации.


В дальнейшем будет дополнено как запустить через Docker
