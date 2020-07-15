Lab 3: 
# Deploy using Docker compose #
Time : 30 minutes

## Step 1: check docker compose ##
docker-compose -v

## Step 2: create compose file ##
$ cat > docker-compose.yml  <br/>
{code}  <br/>
ctl + c	  <br/>

## Step 3: update database connection  ##
$ vi app.py   <br/>
goto line 7 and update ip address   <br/>
client = MongoClient("mongodb://todoDB:27017")   <br/>
:wq

## Step 4: build , push ## 
$ docker build -t getmub/myapi .   <br/>
$ docker push getmub/myapi  <br/>

## Step 5:run ##
$ docker-compose up -d 
$ curl --header "Content-Type: application/json" --request POST  --data '{"desc":"buy beer"}'  http://localhost:5000/add  <br/>
$ curl http://127.0.0.1:5000/get  <br/>

## Step 6:clean ##
$ docker-compose down
$ docker system prune -a  <br/>
