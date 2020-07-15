Lab 1: Create Micrservice Api and deploy in Docker
Time : 30 minutes

Step 1: Create a Docker Account
https://hub.docker.com/

Step 2: login to lab
https://labs.play-with-docker.com/

Step 3: create files
$ mkdir myapi
$ cd myapi

myapi
└───requirements.txt
│
└───Dockerfile
│
└───app.py

Step 4:
$ cat > app.py
from flask import Flask

app = Flask(__name__)

@app.route("/add", methods = ['POST'])
def add_contact() :
    data = json.loads(request.data)
    desc = data['desc']
    if desc :
        # insert in database
        return dumps({ 'message' : 'SUCCESS' })
        
@app.route("/get", methods = ['GET'])
def get_all_contact() :
    # get from database
    return { '0':{'desc': 'buy grocery'},'1' : {'desc': 'pay bills'} }

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')


Step 5: 
$ cat > requirements.txt
flask
pymongo

flask_restful
	
Step 6:
$ cat > Dockerfile

FROM python:3.7

RUN mkdir /myapi
WORKDIR /myapi
ADD . /myapi/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/myapi/app.py"]

Step 7:
$ docker build -t myapi:latest .
$ docker images
$ docker run -d -p 5000:5000 myapi:latest
$ docker ps
$ curl http://127.0.0.1:5000/
$ docker login -u getmub
$ docker tag myapi:latest getmub/myapi
$ docker push getmub/myapi
$ docker ps
$ docker kill 34144376516a
$ docker system prune -a
$ docker pull getmub/myapi
$ docker images
$ docker run -d -p 5000:5000 getmub/myapi
$ curl http://127.0.0.1:5000/
