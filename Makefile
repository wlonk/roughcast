-include .env
export $(shell sed 's/=.*//' .env 2> /dev/null || true)

######
# Basic Utilities
###

.PHONY: default
default:
	yarn serve

.PHONY: prepare-prod
prepare-prod: install migrate build static

.PHONY: serve-prod
serve-prod:
	gunicorn roughcast.wsgi

.PHONY: clean
clean:
	rm -rf staticfiles/*
	rm -rf dist/*
	rm -rf coverage/
	rm -rf .coverage
	rm -rf htmlcov/

######
# Managing Dependencies
###

.PHONY: lock
lock: requirements/base.txt requirements/dev.txt

requirements/dev.txt: requirements/base.txt

%.txt: %.in
	pip-compile --upgrade --output-file=$@ $<

.PHONY: install-py
install-py:
	# Install packages into the local context
	# (make sure to activate that virtual environment!)
	pip install pip-tools
	pip-sync requirements/base.txt

.PHONY: install-dev
install-py-dev: install-py
	# Install packages into the local context
	# (make sure to activate that virtual environment!)
	pip-sync requirements/base.txt requirements/dev.txt

.PHONY: install-js
install-js:
	yarn install

.PHONY: install
install: install-js install-py

######
# Managing the Database
###

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

.PHONY: migratezero
migrate-zero:
	python manage.py migrate roughcast zero

.PHONY: user
user:
	python manage.py createsuperuser

.PHONY: dumpdata
dumpdata:
	python manage.py dumpdata -o roughcast/fixtures/test.json roughcast

.PHONY: loaddata
loaddata:
	python manage.py loaddata test.json

######
# Manage Static Assets
###

.PHONY: static
static:
	python manage.py collectstatic --noinput

.PHONY: build
build:
	yarn build

######
# Testing and Linting
###

.PHONY: test-pdb
test-pdb:
	pytest --pdb

.PHONY: test-py
test-py:
	pytest

.PHONY: test-js
test-js:
	yarn test

.PHONY: test
test: test-py test-js

.PHONY: lint-py
lint-py:
	isort -rc manage.py roughcast tests
	black manage.py roughcast tests
	flake8 manage.py roughcast tests

.PHONY: lint-js
lint-js:
	yarn lint

.PHONY: lint
lint: lint-py lint-js

######
# Development Conveniences
###

.PHONY: shell
shell:
	python manage.py shell

.PHONY: dbshell
dbshell:
	python manage.py dbshell
