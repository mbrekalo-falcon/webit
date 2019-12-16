install-packages:
	pip install -r requirements.txt

run:
	envdir .envdir python manage.py runserver

makemigrations:
	envdir .envdir python manage.py makemigrations -n $(argument)

migrate:
	envdir .envdir python manage.py migrate

collect:
	envdir .envdir python manage.py collectstatic