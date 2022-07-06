FROM ubuntu:latest

MAINTAINER WOrLaF

LABEL version='1.0'

RUN apt-get update
RUN apt-get install -y python3


WORKDIR /FastApi_basic_project

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 8000

CMD ["uvicorn", "workshop.app:app", "--host", "0.0.0.0"]