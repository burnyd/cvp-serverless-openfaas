FROM ubuntu:xenial
ENTRYPOINT []

ADD . /src
RUN apt-get update && apt-get install python-pip -y
RUN pip install cvprac requests urllib3   

ENTRYPOINT ["python", "/src/cvpserverlessargv.py"]


