tag=latest
organization=mlworkshops
image=data-science-interview-workshop
run_options=-p 8888:8888 -v `pwd`:/workshop/

# Docker
build:
	@docker build --force-rm -t $(image) ./
	@docker tag $(image) $(organization)/$(image):$(tag)

docker-run:
	@docker run -it --rm $(run_options) $(organization)/$(image):$(tag) $(cmd)

docker-push:
	@docker push $(organization)/$(image):$(tag)

pull:
	@docker pull $(organization)/$(image):$(tag)


.PHONY: help
help:
	@echo "\nDocker:"
	@echo " build                    Build a docker image"
	@echo " docker-run               Run a docker image locally"
	@echo " docker-tag               Tag a local docker image (before pushing it to dockerhub)"
	@echo " docker-push              Push a tagged docker image to dockerhub"

