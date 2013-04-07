SHELL := /bin/bash

help:
	@echo "usage:"
	@echo "    make deploy -- deploy to heroku"

deploy:
	git push heroku master
