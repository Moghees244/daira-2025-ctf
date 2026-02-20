FROM python:alpine3.17
RUN apk add --no-cache figlet
WORKDIR /Web_App1
COPY . /Web_App1
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "run.py"]
