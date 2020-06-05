include .env
export $(shell sed 's/=.*//' .env)

# Run server:
.PHONY: default
default:
	python manage.py runserver

# Deploy!
.PHONY: deploy
deploy:
	echo "Not implemented"

# Lock requirements files:
.PHONY: lock
lock: requirements/base.txt requirements/dev.txt

requirements/dev.txt: requirements/base.txt

%.txt: %.in
	pip-compile --output-file=$@ $<

# Install packages into the local context
# (make sure to activate that virtual environment!)
.PHONY: install
install:
	pip install -r requirements/base.txt
	pip install -r requirements/dev.txt

# Handle DB state, making and applying migrations
.PHONY: migrations
migrations:
	python manage.py makemigrations roughcast

.PHONY: data-migrations
data-migrations:
	python manage.py makemigrations --empty roughcast

.PHONY: merge-migrations
merge-migrations:
	python manage.py makemigrations roughcast --merge

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: user
user:
	python manage.py createsuperuser

# Manage static assets:
.PHONY: static
static:
	python manage.py collectstatic --noinput

# Run tests:
.PHONY: test
test:
	pytest

# Run linting tools:
.PHONY: lint
lint:
	isort -rc manage.py roughcast tests
	black manage.py roughcast tests
	flake8 manage.py roughcast tests

# Access Python shell
.PHONY: shell
shell:
	python manage.py shell

# Access Postgres shell
.PHONY: dbshell
dbshell:
	python manage.py dbshell

# Debug Django URLs
.PHONY: show_urls
show_urls:
	python manage.py show_urls
