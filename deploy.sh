	#!/bin/bash
    DOCKER_COMPOSE=true bash <(curl -s https://raw.githubusercontent.com/zalando-incubator/docker-locust/master/local.sh) deploy \
	--target=https://inlyt6uoh8.execute-api.ap-southeast-1.amazonaws.com/ \
	--locust-file=./test-scripts/main.py \
	--slaves=1 \
	--mode=manual