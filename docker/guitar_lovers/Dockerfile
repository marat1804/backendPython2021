FROM python:3.9-buster

RUN mkdir /app
ADD . /app/
WORKDIR /app/
RUN pip install -r /app/requirements.txt

RUN chmod +x /app/run.sh
RUN sed -i 's/\r$//g' /app/run.sh
