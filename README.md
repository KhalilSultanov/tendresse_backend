## TENDRESSE Backend

Backend для интернет-магазина TENDRESEE (еще в разработке).

## Настройка проекта:

### Установка виртуального окружения (Virtual Environment)
Если у вас нет установленного virtualenv, установите его с помощью pip:

<code>pip install virtualenv</code>

Затем создайте и активируйте виртуальное окружение:

Создание: <code>virtualenv venv</code>

Активация для Linux/MacOS: <code>source venv/bin/activate</code>

Активация для Windows: <code>venv\Scripts\activate</code>  # Для Windows

### Установка зависимостей

Убедитесь, что вы находитесь в активированном виртуальном окружении, и установите зависимости из requirements.txt:

<code>pip install -r requirements.txt</code>

Также стоит учесть, что для в проекте испульзуется Django 5.0.1, следовательно минимальные версии вашего Python 3.10, 3.11, 3.12.

### Применение миграций

Выполните миграции для создания базы данных:

<code>python manage.py makemigrations</code>

<code>python manage.py migrate</code>

### Запуск сервера

<code>python manage.py runserver</code>