#!/usr/bin/env bash

# In a Podman pod, the system doesn't actually route traffic to a specific container by name or ID. 
# Instead, it routes the traffic to the pod's shared network, and whichever container is actively listening on that port receives the traffic.
podman pod exists memgraph || podman pod create --name memgraph -p 3000:3000

podman run -dt --pod memgraph --rm --name memgraph-mage \
  docker.io/memgraph/memgraph-mage --schema-info-enabled=True

podman run -dt --pod memgraph --rm --name lab \
  -e QUICK_CONNECT_MG_HOST=localhost \
  -e CONFIG_URI=file:///home/lab/config.yaml -v /home/ben/src/memgraph-lab/config.yaml:/home/lab/config.yaml \
  docker.io/memgraph/lab
