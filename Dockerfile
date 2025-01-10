FROM python:latest

RUN apt-get update -y && apt-get upgrade -y

RUN pip3 install -U pip setuptools
RUN pip3 install -U -r requirements.txt

CMD ["python3","-m","FallenRobot"]
