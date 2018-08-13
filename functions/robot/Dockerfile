FROM ubuntu:xenial
ENTRYPOINT []

ADD https://github.com/openfaas/faas/releases/download/0.8.5/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog
COPY . .
RUN apt-get update && apt-get install -y python python-pip
RUN pip install network_validation-1.0.1.tar.gz requests
RUN chmod +x entry.sh
ENV fprocess="./entry.sh"

CMD ["fwatchdog"]

