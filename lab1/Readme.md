Lab 1: 
# Create Micrservice Api and deploy in Docker #
Time : 30 minutes

## Step 1: Create a Docker Account ##
https://hub.docker.com/ <br/>
$ docker login -u getmub  <br/>

## Step 2: login to lab ##
https://labs.play-with-docker.com/

## Step 3: create files ##
mkdir myapi <br/>
cd myapi <br/>
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab1/server.js  <br/>
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab1/package.json <br/>
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab1/Dockerfile <br/>

## Step 4: build ##  
synatax : docker build docker_id/microservice_name:version <directory of files>  <br/>
docker build -t getmub/dateapi:v1 .  <br/>
docker images  <br/>

## Step 5: push to hub ##
docker push getmub/dateapi:v1  <br/>

## step 6: run from hub ##
$ docker run -d -p 8080:8080 getmub/dateapi:v1  <br/>
<br/>
-d is to detach the terminal from the container process (run it in the background) <br/>
--name is to specify a name for the container <br/>
-p local:container is to forward traffic from a local port to a port in the container <br/>

Get container ID <br/>
$ docker ps  <br/>
Print app output  <br/>
$ docker logs <container id>  <br/>
$ curl http://127.0.0.1:8080/date  <br/>

Enter the container  <br/>
$ docker exec -it container_id /bin/bash  <br/>

## step 7: clean ##
$ docker ps  <br/>
$ docker kill container_id  <br/>
$ docker rmi --force image_id <br/>
$ docker system prune -a  <br/>
{ remove image from hub.docker.com }
