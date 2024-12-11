FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app/

