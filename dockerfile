#from alpine:latest as base
from python:3.7.3-alpine as base

from base as builder

RUN apk add --no-cache python3 python3-dev py-pip build-base

# create directory to copy files to
RUN mkdir /install/
WORKDIR /install

# copy the files that should have come from git
copy requirements.txt requirements.txt

# go ahead and install the python modules that also came from git
RUN pip install --install-option="--prefix=/install" -r requirements.txt

FROM base

copy --from=builder /install /usr/local
RUN mkdir /app/

copy *.py /app/

WORKDIR /app/
RUN pytest


# create a simple python script
#RUN echo print("Hello World from python from a container!") > c:\hello.py

# establish what command will run when the docker run command is executed
CMD ["python", "/app/main.py"]
