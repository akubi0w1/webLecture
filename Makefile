initmigrate:
	# マイグレーション
	docker-compose run --rm app python manage.py makemigrations
	docker-compose run --rm app python manage.py migrate

createsuperuser:
	docker-compose run --rm app python manage.py createsuperuser