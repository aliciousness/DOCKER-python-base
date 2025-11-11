FROM aliciousness/python-base:3.13-debian AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

LABEL maintainer="Richard Craddock richard.craddock@gce.com"
LABEL version=$IMAGE_VERSION
ARG IMAGE_VERSION
ENV IMAGE_VERSION=$IMAGE_VERSION

# Installing necessary packages to install Tensorflow
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  python3-dev \
  libhdf5-dev \
  pkg-config \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Upgrade pip3 and install all python dependencies from requirements.txt file
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /tmp/requirements.txt

# Copy over all scripts to /usr/local/bin/ and make them executable and move gunicorn_conf.py to root
COPY scripts/* /usr/local/bin/
RUN chmod +x /usr/local/bin/* && mv /usr/local/bin/gunicorn_conf.py /gunicorn_conf.py

# copy over app directory with main.py and set to workdir
COPY ./app /app

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["start-gunicorn"]
