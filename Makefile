.PHONY: all clean build image run

NAME=py-ms-boilerplate
VERSION=latest

image:
	docker build -t=$(NAME):$(VERSION) .

run:
	docker run -d -p 5000:5000 --name $(NAME) -e MYSQL_URL="" $(NAME)