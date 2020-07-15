Lab 3: 
# Deploy using Docker compose #
Time : 30 minutes

## Step 1: check docker compose ##
docker-compose -v

## Step 2: create compose file ##
$ cat > docker-compose.yml  <br/>
{code}  <br/>
ctl + c	  <br/>

## Step 3:run ##
$ docker-compose up -d <br/>
$ curl --header "Content-Type: application/json" --request POST  --data '{"desc":"buy beer"}'  http://localhost:5000/add  <br/>
$ curl http://127.0.0.1:5000/get  <br/>

## Step 4: debug ##
Seeing all of the logs from the application deployed.<br/>
$ docker-compose logs <br/>
    
## Step 5:clean ##
$ docker-compose down <br/>
$ docker system prune -a  <br/>
