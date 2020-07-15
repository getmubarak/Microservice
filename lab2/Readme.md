# Connect Microservice Service to Database  #
Time : 30 minutes

## Step 1: run database ##
$ docker run -d -p 27017:27017 --name mydb mongo

## Step 2: get IP address of database container ##
docker inspect mydb | grep IPAddress

## Step 3: update code and update ip address ##
$ cat > app.py  <br/>
{code}  <br/>
ctl + c	  <br/>
$ vi app.py
goto line 7 and update ip address
client = MongoClient("172.17.0.3:27017/")
:wq
## Step 4: build ##  
$ docker build -t myapi:latest .   <br/>
$ docker images  <br/>

## Step 5: push to hub ##
$ docker tag myapi:latest getmub/myapi  <br/>
$ docker push getmub/myapi  <br/>

## step 6: run from hub ##
$ docker run -d -p 5000:5000 getmub/myapi  <br/>
$ docker ps  <br/>
$ curl --header "Content-Type: application/json" --request POST  --data '{"desc":"buy beer"}'  http://localhost:5000/add  <br/>
$ curl http://127.0.0.1:5000/get  <br/>

## step 7: clean ##
$ docker ps  <br/>
$ docker kill container_id  <br/>
$ docker rmi --force image_id <br/>
$ docker system prune -a  <br/>
{ remove image from hub.docker.com }
