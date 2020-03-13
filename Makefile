update_core:
	git checkout master
	git pull
	docker-compose -f production.yml build
	docker-compose -f production.yml up -d
	docker-compose -f production.yml exec django python manage.py migrate
