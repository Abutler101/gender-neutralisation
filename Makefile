SHELL := bash

API_IMAGE_NAME := alexis-turintech/gender-neutralisation-api
APP_IMAGE_NAME := alexis-turintech/gender-neutralisation-app

build: ## Build the container
	docker image build -t $(API_IMAGE_NAME) -f api.Dockerfile .
	docker image build -t $(APP_IMAGE_NAME) -f app.Dockerfile .

deploy: build ## Deploy all services
	docker-compose up -d

deploy-cache: ## Only deploy redis server
	docker-compose up --scale neutralisation-api=0 -d

down:
	docker-compose down
