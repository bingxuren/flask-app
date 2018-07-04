FROM ubuntu:latest

MAINTAINER Bingxu Ren "bingxuren88@gmail.com"


RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN . venv/bin/activate
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["demo.py"]