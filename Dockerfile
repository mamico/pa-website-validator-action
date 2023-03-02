# Base image built from Dockerfile.base (Chrome Stable + Node LTS)
FROM node:lts-buster-slim

LABEL "com.github.actions.name"="PA Website Validator Audit"
LABEL "com.github.actions.description"="Run tests on a webpage via Italia PA Website Validator"
LABEL "com.github.actions.icon"="check-square"
LABEL "com.github.actions.color"="yellow"

LABEL version="0.0.1"
LABEL repository="https://github.com/mamico/pa-website-validator-action"
LABEL homepage="https://github.com/mamico/pa-website-validator-action"
LABEL maintainer="Mauro Amico <mauro.amico@gmail.com>"

# Cache bust to ensure latest version when building the image
ARG CACHEBUST=1

ARG DEBIAN_FRONTEND=noninteractive

# TODO: instead of chromium package, install only pupeeter's prerequisities?
RUN apt-get update -qqy \
  && apt-get -qqy install \
       chromium \
       dumb-init gnupg wget ca-certificates apt-transport-https \
       ttf-wqy-zenhei \
       git jq bc \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Download latest pa-website-validator build from npm
# RUN npm install -g pa-website-validator

# Download master or tag from github
# RUN git clone --branch develop https://github.com/mamico/pa-website-validator && \
RUN git clone --branch v2.0.0 https://github.com/italia/pa-website-validator && \
     cd pa-website-validator && \
     npm install && \
     npm install -g .

# RUN npm install -g https://github.com/italia/pa-website-validator.git

# Download latest or released pa-website-validator from https://github.com/italia/pa-website-validator/releases
# https://github.com/italia/pa-website-validator/releases/download/v1.0.10/comuni-1.0.10-Linux-x64.zip
# https://github.com/italia/pa-website-validator/releases/download/v1.0.10/scuole-1.0.10-Linux-x64.zip

# Disable Lighthouse error reporting to prevent prompt
ENV CI=true

RUN useradd headless --shell /bin/bash --create-home \
  && usermod -a -G sudo headless \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && echo 'headless:nopassword' | chpasswd
RUN mkdir /report && chown -R headless:headless /report
USER headless

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
