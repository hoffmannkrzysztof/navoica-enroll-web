ifeq ($(ENROLL_DOMAIN),)
  $(error ENROLL_DOMAIN is not set)
endif

ifeq ($(ENROLL_EMAIL),)
  $(error ENROLL_EMAIL is not set)
endif

RANDOM_STRING := $(shell openssl rand -hex 24)

update:
	git checkout master
	git pull
	docker-compose -f production.yml build
	docker-compose -f production.yml up -d
	@echo "waiting 10sec for postgresql to boot up"
	sleep 10
	docker-compose -f production.yml exec django python manage.py migrate
	docker-compose -f production.yml exec django python manage.py collectstatic --noinput --clear

setup:
	rm -rf .envs/.production/ || true
	rm compose/production/traefik/traefik.yml || true

	cp -av .envs/.production_example/ .envs/.production/
	sed -i "" "s/__DOMAIN__/${ENROLL_DOMAIN}/g" '.envs/.production/.django'
	sed -i "" "s/__DJANGO_SECRET_KEY__/${RANDOM_STRING}/g" '.envs/.production/.django'


	cp compose/production/traefik/traefik.yml.example compose/production/traefik/traefik.yml
	sed -i "" "s/__DOMAIN__/${ENROLL_DOMAIN}/g" 'compose/production/traefik/traefik.yml'
	sed -i "" "s/__EMAIL__/${ENROLL_EMAIL}/g" 'compose/production/traefik/traefik.yml'

	docker-compose -f production.yml build
	docker-compose -f production.yml up -d
	@echo "waiting 10sec for postgresql to boot up"
	sleep 10
	docker-compose -f production.yml exec django python manage.py migrate
	docker-compose -f production.yml exec django python manage.py collectstatic  --noinput --clear
	docker-compose -f production.yml exec django python manage.py createsuperuser --email ${ENROLL_EMAIL} --username admin

destroy:
	docker-compose -f production.yml down -v

stop:
	docker-compose -f production.yml stop

start:
	docker-compose -f production.yml up -d
	@echo "waiting 10sec for postgresql to boot up"
	sleep 10
	docker-compose -f production.yml exec django python manage.py migrate
	docker-compose -f production.yml exec django python manage.py collectstatic --noinput --clear
