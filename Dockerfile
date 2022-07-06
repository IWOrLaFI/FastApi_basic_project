# Dockerfile

# pull the official docker image
FROM python

WORKDIR /FastApi_basic_project

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 8000

CMD ["uvicorn", "workshop.app:app", "--host", "0.0.0.0"]
