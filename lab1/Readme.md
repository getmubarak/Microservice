Lab 1: 
# Create Micrservice Api and deploy in Docker #
Time : 30 minutes

## Step 1: Create a Docker Account ##
https://hub.docker.com/

## Step 2: login to lab ##
https://labs.play-with-docker.com/

## Step 3: create files ##
$ mkdir myapi <br/>
$ cd myapi <br/>
$ cat > app.py  <br/>
{code}  <br/>
ctl + c	  <br/>
$ cat > requirements.txt  <br/>
{code}  <br/>
ctl+c  <br/>
$ cat > Dockerfile  <br/>
{code}  <br/>
ctl+c  <br/>
## Step 4: build ##  
$ docker build -t myapi:latest .   <br/>
$ docker images  <br/>

## Step 5: push to hub ##
$ docker login -u getmub  <br/>
$ docker tag myapi:latest getmub/myapi  <br/>
$ docker push getmub/myapi  <br/>

## step 6: run from hub ##
$ docker run -d -p 5000:5000 getmub/myapi  <br/>
$ docker ps  <br/>
$ curl --header "Content-Type: application/json" --request POST  --data '{"desc":"buy beer"}'  http ://localhost:5000/add  <br/>
$ curl http://127.0.0.1:5000/  <br/>

## step 7: remove local image ##
$ docker ps  <br/>
$ docker kill 34144376516a  <br/>
$ docker system prune -a  <br/>

