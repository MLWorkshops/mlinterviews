tag=latest
statsimage=stats-workshop
organization=mlworkshops
image=data-science-interview-workshop

# Docker
build:
	@docker build --force-rm $(options) -t $(statsimage) ./

docker-run:
	@docker run -it --rm $(options) $(statsimage):$(tag) $(cmd)

docker-tag:
	@docker tag $(statsimage):$(tag) $(organization)/$(image):$(tag)

docker-push:
	@docker push $(organization)/$(image):$(tag)
