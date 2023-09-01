<<<<<<< HEAD
# $DEL_BEGIN

# ####### 👇 SIMPLE SOLUTION (x86 and M1) 👇 ########
# FROM python:3.8.12-buster

# WORKDIR /prod

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY taxifare taxifare
# COPY setup.py setup.py
# RUN pip install .

# COPY Makefile Makefile
# RUN make reset_local_files

# CMD uvicorn taxifare.api.fast:app --host 0.0.0.0 --port $PORT

####### 👇 OPTIMIZED SOLUTION (x86)👇 #######

# tensorflow base-images are optimized: lighter than python-buster + pip install tensorflow
FROM tensorflow/tensorflow:2.10.0
# OR for apple silicon, use this base image instead
# FROM armswdev/tensorflow-arm-neoverse:r22.09-tf-2.10.0-eigen

WORKDIR /prod

# We strip the requirements from useless packages like `ipykernel`, `matplotlib` etc...
COPY requirements.txt requirements.txt
=======
FROM python:3.10.6-slim

WORKDIR /prod

# First, pip install dependencies
COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

>>>>>>> 736d31fa26ab96eeba835658535937ef2270f201
RUN pip install -r requirements.txt

COPY judgeabook judgeabook
COPY setup.py setup.py
RUN pip install .

<<<<<<< HEAD
COPY Makefile Makefile
RUN make reset_local_files

CMD uvicorn judgeabook.api.api:app --host 0.0.0.0 --port $PORT
# $DEL_END
=======
CMD uvicorn judgeabook.api.fast:app --reload --host 0.0.0.0 --port $BACKEND_PORT
>>>>>>> 736d31fa26ab96eeba835658535937ef2270f201
