Today's practice is about installing and running Memgraph lab on zeus.lan

1. Installing

zeus.lan runs Podman, and its [networking](https://www.redhat.com/en/blog/container-networking-podman) differs from docker. 
So some adjustments to the memgraph [instructions](https://memgraph.com/docs/memgraph-lab/getting-started/installation-and-deployment) are needed.

# in zeus.lan
podman run -dt --pod new:memgraph -p 3000:3000 --rm --name lab memgraph/lab

This starts the lab container in a new podman pod.
Forwards host port 3000 to the container

# start memgraph DB
podman run -dt --pod memgraph --rm --name memgraph-mage memgraph/memgraph-mage

This starts the actual DB in the same pod (so 7687 and 7444 are not required to be exposed).

2. Running

http://zeus.lan:3000 works without authentication.
Loading data is fine through the web interface.

