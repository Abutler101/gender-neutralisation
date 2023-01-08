SHELL := bash

IMAGE_NAME := alexis-turintech/gender-neutralisation

build: ## Build the container
	docker image build -t $(IMAGE_NAME) .

deploy: build ## Deploy all services
	docker-compose up -d

deploy-cache: ## Only deploy redis server
	docker-compose up --scale neutralisation-api=0 -d

down:
	docker-compose down
