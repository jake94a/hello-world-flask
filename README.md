A simple flask app

start manually:

- ensure your working directory contains app.py
  - run `ls` and verify `app.py` is in the printed list
- `python3 -m venv venv`
  - creates a virtual environment
- `source venv/bin/activate`
  - activates the virtual environment
- `pip install -r requirements.txt`
  - installs all listed packages into venv
- `flask run`
  - instructs python to run `app.py` within the flask framework
- Navigate to localhost:5000

start via docker:

- `docker build -t hello-world-flask .`
  - instruct docker to build an image
  - tag the image with the name "hello-world-flask"
  - build the image from the current working directory
- `docker run -p 5000:5000 --env-file dev.env hello-world-flask`
  - instruct docker to run the hello-world-flask image in a new container
  - publish the output of the container to port 5000
    - publish `<host>:<container>`
  - instruct docker to load the environment variables found in dev.env
- navigate to localhost:5000

dockerignore:

- instruct `docker build` to ignore files and/or directories
