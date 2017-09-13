runserver:
	./source/manage.py runserver

migrate:
	./source/manage.py migrate

createsuperuser:
	./source/manage.py createsuperuser

test:
	cd ./source && pytest

rodar_verificacoes:
	./source/manage.py rodar_verificacoes
