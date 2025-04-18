#!/bin/sh
docker rm -f store
docker run \
-e APP_PORT=8001 \
--network=host \
--restart=always \
--name=store \
--detach=true \
store:1.0.0
