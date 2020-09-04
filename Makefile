include .env
export $(shell sed 's/=.*//' .env)

# Run server:
.PHONY: default
default:
	yarn serve

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

.PHONY: install-dev
install-dev: install
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

.PHONY: migratezero
migratezero:
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

# Manage static assets:
.PHONY: static
static:
	python manage.py collectstatic --noinput

.PHONY: build
build:
	yarn build

# Run tests:
.PHONY: test
test:
	pytest
	yarn test

# Run linting tools:
.PHONY: lint
lint:
	isort -rc manage.py roughcast tests
	black manage.py roughcast tests
	flake8 manage.py roughcast tests
	yarn lint

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

.PHONY: prepare-prod
prepare-prod: install migrate build static
