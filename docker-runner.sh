docker stop flask-test
docker rm flask-test
docker build . flask:latest
docker run -d --network=host --name=flask-test flask
docker logs -f flask-test
