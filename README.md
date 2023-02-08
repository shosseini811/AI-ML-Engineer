# Overview
This template provides a very basic Flask application. This is intended to provide a bare minimum set of files that is executable, and can be compiled into a functional docker image.

This code creates two endpoints using Flask: /api/supervisors and /api/submit. 
The /api/supervisors endpoint makes a GET request to the specified AWS API, 
formats the response to return a list of supervisors in the desired format, 
and sorts the supervisors in alphabetical order. 

The /api/submit endpoint retrieves personal information from the form data, prints it to the console, 
and returns a success status code if all the required parameters (firstName, lastName, and supervisor) 
are provided, or returns an error status code if any of the required parameters is missing.


# Running locally with pip and flask
This project has been tested with python 3.
```
pip install -r requirements.txt
flask run
```

# Running with docker
To help ensure consistently correct startup across multiple platforms, you may choose to use Docker to containerize your application.  Installation steps for docker can be found on their main page.
https://docs.docker.com/engine/install/

With Docker installed, you can build your a new image. This build needs to be run after any changes are made to the source code.
```
docker build --tag=flask-template:latest .
```

After the image builds successfully, run a container from that image.
```
docker run -d --name flask-template -p5000:5000 flask-template:latest
```

Test the container has successfully started.
```
curl localhost:5000/
```

When you are done testing, stop the server and remove the container.
```
docker rm -f flask-template
```

# Running with docker-compose
```
docker-compose up --build
```