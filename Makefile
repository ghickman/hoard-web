SHELL := /bin/bash

help:
	@echo "usage:"
	@echo "    make deploy -- deploy to heroku"
	@echo "    make static -- build static files to s3"

deploy:
	git push heroku master

static:
	STATICFILES_STORAGE='storages.backends.s3boto.S3BotoStorage' python manage.py collectstatic --noinput
