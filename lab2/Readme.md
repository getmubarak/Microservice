# Connect Microservice Service to Database  #
Time : 30 minutes

## Step 1: create network ##
$ docker network create mynet
$ docker network ls

## Step 2: run database ##
$ docker run --name todoDB --network=mynet -v /root/myapi/mydata:/data/db -p 27017:27017 -d mongo

## Step 3: get IP address of database container ##
docker inspect todoDB | grep IPAddress

## Step 4: update code and update ip address ##
$ cat > app.py  <br/>
{code}  <br/>
ctl + c	  <br/>
$ vi app.py
goto line 7 and update ip address
client = MongoClient("172.17.0.3:27017/")
:wq

## Step 5: build , push , run ## 
$ docker build -t getmub/myapi .   <br/>
$ docker push getmub/myapi  <br/>
$ docker run --name myapi --network=mynet -d -p 5000:5000 getmub/myapi  <br/>
$ curl --header "Content-Type: application/json" --request POST  --data '{"desc":"buy beer"}'  http://localhost:5000/add  <br/>
$ curl http://127.0.0.1:5000/get  <br/>

## step 6: clean ##
$ docker ps  <br/>
$ docker kill container_id  <br/>
$ docker images
$ docker rmi --force image_id <br/>
$ docker system prune -a  <br/>
$ docker network disconnect -f mynet todoDB
$ docker network rm mynet
{ remove image from hub.docker.com }
