THIS_FILE := $(lastword $(MAKEFILE_LIST))
.DEFAULT_GOAL := help
DOCKER_COMPOSE_FILE ?= docker-compose.yml

help: ## Show all make commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
build: ## Build containers
	docker-compose -f $(DOCKER_COMPOSE_FILE) build $(c)
up: ## Start all containers in foreground
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d $(c)
start: ## Start all containers in background
	docker-compose -f $(DOCKER_COMPOSE_FILE) start $(c)
down: ## Stop all containers
	docker-compose -f $(DOCKER_COMPOSE_FILE) down $(c)
status: ## Show status of containers
	docker-compose -f $(DOCKER_COMPOSE_FILE) ps
stop: ## Stop all containers
	docker-compose -f $(DOCKER_COMPOSE_FILE) stop $(c)
restart: ## Restart all containers
	docker-compose -f $(DOCKER_COMPOSE_FILE) stop $(c)
	docker-compose -f $(DOCKER_COMPOSE_FILE) up -d $(c)
logs: ## Show all containers logs
	docker-compose -f $(DOCKER_COMPOSE_FILE) logs --tail=100 -f $(c)

logs-web: ## Show web container logs
	docker-compose -f $(DOCKER_COMPOSE_FILE) logs --tail=100 -f web
login-web: ## Login in web container
	docker-compose -f $(DOCKER_COMPOSE_FILE) exec web /bin/bash
createsuperuser: ## Creating super user in web container
	docker-compose -f $(DOCKER_COMPOSE_FILE) exec web python src/manage.py createsuperuser
makemigrations: ## making migrations in web container
	docker-compose -f $(DOCKER_COMPOSE_FILE) exec web python src/manage.py makemigrations
migrate: ## migrate migrations in web container
	docker-compose -f $(DOCKER_COMPOSE_FILE) exec web python src/manage.py migrate
black-flake8: ## for code style and correcting code
	docker-compose -f $(DOCKER_COMPOSE_FILE) exec web black --line-length=99 . && flake8 --ignore=E203,E501,W503,B008,E266
db-shell: ## Login to db shell container
	docker-compose -f $(DOCKER_COMPOSE_FILE) exec db psql -U postgres