FROM python:3.10.6-slim

WORKDIR /prod

# First, pip install dependencies
COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN pip install -r requirements.txt

COPY judgeabook judgeabook
COPY setup.py setup.py
RUN pip install .

CMD uvicorn judgeabook.api.fast:app --reload --host 0.0.0.0 --port $BACKEND_PORT
