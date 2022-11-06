#
# Necati REST API service (Makefile)
#

all: clean build test logs

clean:
	docker volume prune -f
	docker volume rm $(docker volume ls -q) 2>/dev/null || :
	rm -rf vol-mongodb src/__pycache__/ && mkdir vol-mongodb && touch vol-mongodb/.gitkeep
	docker system prune -a -f && docker builder prune -a -f
	docker container prune --force
	docker stop $(docker ps -a -q) 2>/dev/null || :
	docker rm $(docker ps -a -q) 2>/dev/null || :
	docker rmi $(docker ps -a -q) 2>/dev/null || :
	docker rmi $(docker images -a -q) 2>/dev/null || :
	docker-compose down --rmi all -v --remove-orphans
	docker ps -a
	docker-compose ps -a

build:
	docker-compose up --build --force-recreate --no-deps -d database
	docker-compose up --build --force-recreate --no-deps -d api

run:
	docker-compose up -d database
	docker-compose up -d api

test:
	@echo "Waiting for all services ..."
	@sleep 5
	@curl -i http://localhost:9090/get_output
	@curl -i -H "Content-Type: application/json" -X POST -d '{"cmd": "Necati API first entry for testing"}' http://localhost:9090/new_task
	@curl -i http://localhost:9090/get_output

logs:
	docker logs --tail 1000 -f necati-api
