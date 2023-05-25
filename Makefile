server:
	python manage.py migrate && python manage.py runserver

migrations:
	python manage.py makemigrations

# checkmigrations:
# 	python manage.py makemigrations --check --no-input --dry-run
