Docker swarm gotchas:


-images need to be pre built before deploy
  -built custom image with web app and jmx exporter before using the big docker-compose file
  -docker-compose -f docker-compose-build.yml build
  - -f for giving a file name for compose (else will default to docker-compose.yml)
  - does assume that there is a file named 'Dockerfile' in the current working directory
  
-in order for services to go on all nodes, including masters and workers must use: mode: global
  - see docker-compose.yml for node-exporter
  
 -docker login error, something about docker defaulting to secretservice and will change to using pass
  - error getting credentials - err: exit status 1, out: `Cannot autolaunch D-Bus without X11 $DISPLAY
  - sudo apt install gnupg2 pass
  - gpg2 --full-generate-key
  - gpg2 -k
  - pass init "[uid returned from above commands]"
  -https://stackoverflow.com/questions/51222996/docker-login-fails-on-a-server-with-no-x11-installed


Prometheus gotchas

  - dns discovery is a thing, will discover services by service name, see prometheus.yml
  
  
  
  Helpful commands:
  
  - docker swarm init (from node that will be the master to begin with)
  - docker swarm join --token <big long data string out put from command above> (will add a node the swarm as a worker)
  - docker swarm leave --force (good for bringing down the master when mistakes were made) (also run from worker node)
  - docker service ls (list current services as well as health/errors, number of replicas that are up)
  - docker service ps <service name> (return data for specific service include current node, desired state, current state)
  - docker service ps $(docker service ls -q) (return above for every service)
  - sudo service docker restart (have you made too many networks and just screwed up so many times, getting some pool errors?)
  - docker login (login into your dockerhub so that we can pull down the image, else local images need a registry for master and worker nodes to share images)
  - docker stack deploy -c docker-compose.yml --with-registry-auth magenta (lets deploy onto our nodes!! use the stored creds from docker login, name (magenta here) will be appended to front of service names, networks, etc (magenta_serviceName))
  - docker image ls (what images are have been pulled or built locally??)
  - docker network ls (list current networks, some come of the box, can't rm those)
  - docker system prune -a (get rid of unsued everything)
  - docker ps (see containers on the current node, see docker service ps $(docker service ls -q) for all containers)
  - docker node ls (from master node will return current nodes in the swarm)
  - journalctl -u docker.service | tail -n 100 (oh no, things are going sour, give me some logs)
  - docker network prune (remove unused networks)
  
  

  
  
  
  
