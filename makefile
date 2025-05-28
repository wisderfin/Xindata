run:
	docker-compose up -d
	docker-compose run app sh -c "uv run app"
