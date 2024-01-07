# Социальная сеть для блогеров
Веб-приложение для публикации постов пользователей, с авторизацией, персональными лентами, комментариями, подпиской на пользователей.
Стек: Django, DRF, Django ORM, Unittest, Pytest, Bootstrap, Pythonanyware, React.
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:DEADRINO/yatube_project.git
```

```
cd yatube_project
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
