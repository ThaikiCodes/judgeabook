FROM python:3.10.6-buster

WORKDIR /prod

# First, pip install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Then only, install taxifare!
COPY judgeabook judgeabook
COPY setup.py setup.py
RUN pip install .

# We already have a make command for that!
COPY Makefile Makefile
RUN make reset_local_files

CMD uvicorn judgeabook.api.fast:app --reload --host 0.0.0.0 --port $JUDGEABOOK_PORT
