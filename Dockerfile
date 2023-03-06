# base image
FROM python:3.9-slim-buster

# set the working directory
WORKDIR .

# copy the requirements file into the container
COPY requirements.txt .

# install the requirements
RUN pip install -r requirements.txt

# copy the application code into the container
COPY app_mongo.py .

# expose the port that the Flask app will run on
EXPOSE 5000

ENV FLASK_APP app_mongo.py

# start the Flask app
CMD [ "python", "app_mongo.py"]
