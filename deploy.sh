	#!/bin/bash
    DOCKER_COMPOSE=true bash <(curl -s https://raw.githubusercontent.com/zalando-incubator/docker-locust/master/local.sh) deploy \
	--target=https://HOST \
	--locust-file=./test-scripts/main.py \
	--slaves=1 \
	--mode=manual