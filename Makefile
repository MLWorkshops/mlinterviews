tag=latest
organization=mlworkshops
image=data-science-interview-workshop

# Docker
build:
	@docker build --force-rm $(options) -t $(image) ./

docker-run:
	@docker run -it --rm $(options) $(image):$(tag) $(cmd)

docker-tag:
	@docker tag $(image):$(tag) $(organization)/$(image):$(tag)

docker-push:
	@docker push $(organization)/$(image):$(tag)
