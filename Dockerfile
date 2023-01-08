FROM python:3.8

LABEL maintainer="Alexis Butler <alexis@turintech.ai>"

# set the working directory in the container
WORKDIR /app

# update linux system and install gcc packages
RUN apt-get update && \
    apt-get install -y python3-dev build-essential
# update pip
RUN pip install --upgrade pip
# copy and install PyPI dependencies
COPY ./setup/requirements.txt /setup/requirements.txt
# install pip requirements
RUN pip install -r /setup/requirements.txt

# copy the source code to the working directory
COPY ./src /app/src/
# set Python path
ENV PYTHONPATH="$PYTHONPATH:/app/src"

ENTRYPOINT ["python"]
CMD ["-u", "/app/src/main.py" ]