SHELL := bash

IMAGE_NAME := alexis-turintech/gender-neutralisation

build: ## Build the container
	docker image build -t $(IMAGE_NAME) .

deploy: build
	docker-compose up -d

down:
	docker-compose down
