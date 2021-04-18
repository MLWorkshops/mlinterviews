image=stats-workshop

# Docker
build:
	@docker build --force-rm $(options) -t $(image) ./

docker-run:
	@docker run -it --rm $(options) $(image) $(cmd)
