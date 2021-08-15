FROM ubuntu:20.04 as base

LABEL mantainer="neovasili"
LABEL name="Docker image for deployment"
LABEL version="v1.0.0"

ARG python_ver="3.9"
ARG nodejs_ver="16"

ARG sls_ver="2.53.1"

ARG access_key=""
ARG secret_key=""
ARG aws_region="eu-west-1"

ENV AWS_ACCESS_KEY_ID=${access_key}
ENV AWS_SECRET_ACCESS_KEY=${secret_key}
ENV AWS_REGION=${aws_region}

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir /opt/api

WORKDIR /opt/api

RUN apt-get update \
  && apt-get -y install --no-install-recommends \
    python${python_ver} \
    python3-pip \
    curl
RUN curl -sL https://deb.nodesource.com/setup_${nodejs_ver}.x | bash -
RUN apt-get update \
  && apt-get -y install --no-install-recommends \
    nodejs \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*
RUN npm install --global --unsafe-perm --loglevel=error --no-optional \
    serverless@${sls_ver}

# Backend stage
FROM base as backend

COPY /src ./src
COPY /resources ./resources
COPY package.json ./package.json
COPY serverless.yml ./serverless.yml
COPY schema.graphql ./schema.graphql
COPY requirements.txt ./requirements.txt
COPY .local-arguments.yml.template ./.local-arguments.yml

RUN npm install --unsafe-perm --loglevel=error --no-optional
RUN sls requirements install
