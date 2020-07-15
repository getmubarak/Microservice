# Connect Microservice Service to Database  #
Time : 30 minutes

## Step 1: update code ##
rm app.py <br/>
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab2/app.py <br/>

## Step 2: build , push  ## 
$ docker build -t getmub/myapi .   <br/>
$ docker push getmub/myapi  <br/>

## Step 3: create network ##
$ docker network create mynet
$ docker network ls

## Step 4: run database ##
$ docker run --name todoDB --network=mynet -v /root/myapi/mydata:/data/db -p 27017:27017 -d mongo

## Step 5: get IP address of database container ##
docker inspect todoDB | grep IPAddress

## Step 6: run api  ##
$ docker run --name myapi --env MONGO_HOST=172.19.0.2 --network=mynet -p 5000:5000 -d getmub/myapi  <br/>
$ curl --header "Content-Type: application/json" --request POST  --data '{"desc":"buy beer"}'  http://localhost:5000/add  <br/>
$ curl http://127.0.0.1:5000/get  <br/>

## step 7: clean ##
$ docker ps  <br/>
$ docker kill container_id  <br/>
$ docker images
$ docker rmi --force image_id <br/>
$ docker system prune -a  <br/>
$ docker network disconnect -f mynet todoDB
$ docker network rm mynet
{ remove image from hub.docker.com }
