Lab 2: 
# Create Api Version 2 and deploy in Docker #
Time : 30 minutes

rm server.js

wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab1B/server.js

docker build -t getmub/dateapi:v2 .

docker push getmub/dateapi:v2

docker run -d -p 8090:8080 getmub/dateapi:v2

curl http://127.0.0.1:8090/date
