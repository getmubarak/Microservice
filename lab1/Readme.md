Lab 1: 
# Create Micrservice Api and deploy in Docker #
Time : 30 minutes

## Step 1: Create a Docker Account ##
https://hub.docker.com/

## Step 2: login to lab ##
https://labs.play-with-docker.com/

## Step 3: create files ##
mkdir myapi <br/>
cd myapi <br/>
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab1/app.py  <br/>
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab1/requirements.txt <br/>
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab1/Dockerfile <br/>

## Step 4: build ##  
$ docker build -t myapi:latest .   <br/>
$ docker images  <br/>

## Step 5: push to hub ##
$ docker login -u getmub  <br/>
$ docker tag myapi:latest getmub/myapi  <br/>
$ docker push getmub/myapi  <br/>

## step 6: run from hub ##
$ docker run -d -p 5000:5000 getmub/myapi  <br/>
<br/>
-d is to detach the terminal from the container process (run it in the background) <br/>
--name is to specify a name for the container <br/>
-p local:container is to forward traffic from a local port to a port in the container <br/>

Get container ID <br/>
$ docker ps  <br/>
$ curl --header "Content-Type: application/json" --request POST  --data '{"desc":"buy beer"}'  http://localhost:5000/add  <br/>
$ curl http://127.0.0.1:5000/get  <br/>

Print app output  <br/>
$ docker logs <container id>  <br/>

Enter the container  <br/>
$ docker exec -it <container id> /bin/bash  <br/>

## step 7: clean ##
$ docker ps  <br/>
$ docker kill container_id  <br/>
$ docker rmi --force image_id <br/>
$ docker system prune -a  <br/>
{ remove image from hub.docker.com }
