App project manual

Depends programs `docker`, `docker-compose`

Depends .env files, you need create .env and .env_db
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

## Up project with makefile

```
    # set needed variable for dev
    DOCKER_COMPOSE_FILE=docker-compose.yml
    # for prod
    DOCKER_COMPOSE_FILE=docker-compose_prod.yml
    # up project
    make up
    # for more info about make commands
    make help
```

## Up project with manually
if you wanna up pject on prod use `docker-compose -f docker-compose_prod.yml `instead of `docker-compose`

1. Make Your ENTRYPOINT Scripts Executable

    `sudo chmod +x entrypoint.sh`

2. Up docker compose 

    `docker-compose up`

3. Make migrations and migrate

```
    docker-compose exec web python3 manage.py makemigration
    docker-compose exec web python3 manage.py migrate
```

4. Create super user and collect static

```
    docker-compose exec web python3 manage.py createsuperuser
    docker-compose exec web python3 manage.py collectstatic
```

restart container with command "`docker-compose restart`"


Add systemcd service for docker compose autorestart

1) Create `/etc/systemd/system/docker-compose-app.service` file and write

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
please don't be too hard on me because I haven't written in django templates for a long time, I usually write APIs and I'm very used to it 😅🥲