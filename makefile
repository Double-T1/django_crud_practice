all: server migrate makemigrations
.PHONY: all

server:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makemigrations: 
	poetry run python manage.py makemigrations