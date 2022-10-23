# Сайт публикации рецептов
### Дипломный проект Яндекс Практикум. 

![workflow](https://github.com/fokseex/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Стек технологий

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

Foodgram это онлайн сервис для публикации рецептов. Реализован с помощью 
Django и API (DRF). На сайте можно публиковать рецепты, подписываться на 
публикации, добавлять рецепты в избранное, скачать список продуктов в 
формате txt. Сайт использует: React, Nginx, PostgreSQL, Docker

## Подготовка и запуск проекта
### Склонировать репозиторий:
```
git clone https://github.com/fokseex/foodgram-project-react
```
## Для загрузки на удаленный сервис На примере Ubuntu:
* Выполните вход на удаленный сервер 
```
ssh <username>@<host>
```
* Установите docker:
```
sudo apt install docker.io 
```
* Установите docker-compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
* Локально отредактируйте файл infra/nginx.conf и в строке server_name впишите свой IP
* Скопируйте файлы docker-compose.yml и nginx.conf из директории infra на сервер:
```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```

* Cоздайте .env файл:
    ```
    DB_NAME=<имя базы данных postgres>
    POSTGRES_USER=<пользователь бд>
    POSTGRES_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    DJ_SECRET_KEY=<секретный ключ проекта django>
    ```
* Для работы с Workflow добавьте в Secrets GitHub переменные:
    ```
    DB_NAME=<имя базы данных postgres>
    POSTGRES_USER=<пользователь бд>
    POSTGRES_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    
    DOCKER_USERNAME=<имя пользователя>
    DOCKER_PASSWORD=<пароль от DockerHub>
    
    DJ_SECRET_KEY=<секретный ключ проекта django>

    USER=<username для подключения к серверу>
    HOST=<IP сервера>
    SSH_KEY=<ваш SSH ключ (команда cat ~/.ssh/id_rsa)>
    PASSPHRASE=<пароль для ключа, если он установлен>

    TELEGRAM_TO=<ID чата, в который придет сообщение>
    TELEGRAM_TOKEN=<токен вашего бота>
    ```
    Работа workflow Github Action:
     - Проверка кода PEP8 с помощью плагина flake8
     - Сборка и публикация образа в DockerHub.
     - Развертывание проекта на удаленный сервер.
     - Отправка уведомления в Telegram.  
  
* На сервере соберите docker-compose:
```
sudo docker-compose up -d --build
```
* После успешной сборки на сервере выполните команды (только после первого деплоя):
    - Соберите статические файлы:
    ```
    sudo docker-compose exec backend python manage.py collectstatic --noinput
    ```
    - Примените миграции:
    ```
    sudo docker-compose exec backend python manage.py migrate --noinput
    ```
    - Загрузите ингридиенты  в базу данных (необязательно):  
    *Если файл не указывать, по умолчанию выберется ingredients.json*
    ```
    sudo docker-compose exec backend python manage.py load_ingredients <Название файла из директории data>
    ```
    - Создать суперпользователя Django:
    ```
    sudo docker-compose exec backend python manage.py createsuperuser
    ```
    - Проект будет доступен по вашему IP

## Проект в интернете
Проект запущен и доступен по [адресу](http://84.201.129.152/recipes)