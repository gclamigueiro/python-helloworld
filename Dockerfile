FROM python:3.8
LABEL maintainer="Gabriel Camps"

COPY . /app
COPY Dockerfile /
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
