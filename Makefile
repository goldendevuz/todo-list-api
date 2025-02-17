migration:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
i:
	pip install -r requirements.txt
mig:
	make migration && make migrate
cru:
	python manage.py createsuperuser
run:
	python manage.py runserver 0.0.0.0:8000
startapp:
	python manage.py startapp $(name) && mkdir -p apps && mv $(name) apps/$(name)