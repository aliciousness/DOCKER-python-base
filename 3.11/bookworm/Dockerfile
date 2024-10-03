FROM python:3.11-bookworm AS base

LABEL maintainer="Richard Craddock richard.craddock@gce.com"
LABEL version=$IMAGE_VERSION
ARG IMAGE_VERSION
ENV IMAGE_VERSION=$IMAGE_VERSION

# Disable interaction
ENV DEBIAN_FRONTEND=noninteractive

# Set timezone
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

# seting an arg and then setting that arg as an environment variable
ARG RECREATE_REQUIREMENTS_ARG
ENV RECREATE_REQUIREMENTS=$RECREATE_REQUIREMENTS_ARG

# Update upgrade and install dependencies
RUN apt-get clean && rm -rf /var/lib/apt/lists/* \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -ymq \
    wget \
    curl \
    gettext \
    git \
    unzip \
    vim \
    zip \
    nmap \
    iputils-ping \
    ca-certificates \
    gcc \
    libc6-dev \
    libpq-dev 

# Make zsh the default shell and install oh-my-zsh
# Install syntax highlighting and powerlevel10k plugins for oh-my-zsh
RUN apt update && apt install -y zsh \
    && chsh -s $(which zsh) \
    && sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" \
    && git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k \
    && git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Install the root CA certificate onto the container in the directory needed for the update-ca-certificates command
# `update-ca-certificates` updates locally trusted CA certificates,located on the container at /usr/local/share/ca-certificates. 
# NOTE: This path and command are known to work with Debian and Debain-based distributions.If using outside of that, the command and path may need to be adjusted.
ENV CA_URL=https://gist.githubusercontent.com/aliciousness/c61936e29b3fb4b07c33aa25ae330f6a/raw/e950632b12d809f1ecb6d802e768e3fbbe42d296/gistfile1.txt
RUN curl $CA_URL > /usr/local/share/ca-certificates/root_ca.crt && update-ca-certificates

COPY scripts/* /usr/local/bin/
RUN chmod +x /usr/local/bin/* 

ENTRYPOINT [ "entrypoint" ]