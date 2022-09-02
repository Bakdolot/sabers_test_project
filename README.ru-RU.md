## Запуск проекта локалбно

Зависимости проекта: `docker`, `docker-compose`

Нужные файлы окружения: .env и .env_db
Примеры
```
    # .env example
    DJANGO_SECRET=Your token

    ####  database configs  ####
    DB=some_db
    DB_USER=some_user
    DB_PASSWORD=some_password
    DB_HOST=some_host
    DB_PORT=some_port
```

```
    # .env_db example
    POSTGRES_PASSWORD=some_user
    POSTGRES_USER=some_password
    POSTGRES_DB=some_db
```

## Запуск проекта с makefile

```
    # установка нужной переменной для dev
    DOCKER_COMPOSE_FILE=docker-compose.yml
    # для prod
    DOCKER_COMPOSE_FILE=docker-compose_prod.yml
    # запуск
    make up
    # Для просмотра все команд makefile
    make help
```

## Запуск проекта вручную
Если вы хотите поднять проект prod исползуйте комманды `docker-compose -f docker-compose_prod.yml ` вместо `docker-compose`

1. Сделать ENTRYPOINT Scripts исполняемым

    `sudo chmod +x entrypoint.sh`

2. Запуск проекта

    `docker-compose up`

3. сделать миграции

```
    docker-compose exec web python3 manage.py makemigration
    docker-compose exec web python3 manage.py migrate
```

4. Создание супер пользователя и сборка статиков

```
    docker-compose exec web python3 manage.py createsuperuser
    docker-compose exec web python3 manage.py collectstatic
```

перезагрузить контейнер с помощи команды "`docker-compose restart`"


Добавить systemcd service для docker compose autorestart

1) Создать `/etc/systemd/system/docker-compose-app.service` файл и написать

```
    [Unit]
    Description=Docker Compose Application Service
    Requires=docker.service
    After=docker.service

    [Service]
    WorkingDirectory=/{your project path}
    ExecStart=docker-compose -f docker-compose_prod.yml up
    ExecStop=docker-compose -f docker-compose_prod.yml down
    TimeoutStartSec=0
    Restart=on-failure
    StartLimitIntervalSec=60
    StartLimitBurst=3

    [Install]
    WantedBy=multi-user.target
```

P.S.
пожалуйста не судите строго, потому что я давно не писал на django templates, я обычно пишу API и очень привык к этому 😅🥲