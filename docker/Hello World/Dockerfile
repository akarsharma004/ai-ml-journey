# Important Basic Commands for dockerization
# 
# FROM python:3.8-alpine # Base image should be a linux image
# COPY . /app # this app folder will copyt the all the file in the container as layer
# WORKDIR /app
# RUN pip install -r requirements.txt
# CMD python app.py
FROM python:3.8-alpine 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py