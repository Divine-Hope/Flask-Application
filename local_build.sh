docker stop $(docker ps -aqf "name=flask_app")
docker build -t flask_app .
docker run --rm -it --name flask_app -p 5000:5000 flask_app:latest
