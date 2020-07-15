FROM python:3.7

RUN mkdir /myapi
WORKDIR /myapi
ADD . /myapi/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/myapi/app.py"]
