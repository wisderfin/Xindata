include .env
export $(shell sed -E '/^\s*#/d;/^\s*$$/d;s/=.*//' .env) # import all variables from .env

first-run:
	docker-compose up --build -d --remove-orphans
	docker-compose exec ollama ollama pull ${LLM_MODEL}
	docker-compose run app sh -c "uv run app"

run:
	docker-compose up -d
	docker-compose run app sh -c "uv run app"
