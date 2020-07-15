Lab 3: 
# Deploy using Docker compose #
Time : 30 minutes

## Step 1: Create a Docker Account ##
docker-compose -v

## Step 2: create compose file ##
$ cat > docker-compose.yml  <br/>
{code}  <br/>
ctl + c	  <br/>

## Step 3: update database connection  ##
$ vi app.py
goto line 7 and update ip address
client = MongoClient("mongodb://todoDB:27017")
:wq

