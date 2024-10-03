# Docker-python-base

This Docker image is based on Python 3.11. It's designed to provide a development environment with a set of utilities and configurations.

[Docker hub]

# Supported tags and respective Dockerfile links

- [`v1.3-3.20-bookworm-slim-python`, `v1.3-python3-debian`, `v1.3-slim`, `latest`, `python`]

- [`v1.3-python3.20-bookworm`, `v1.3-python3-bookworm`,`v1.3-bookworm`]

## Features

- **Node.js**: The base image is Node.js version
- **Utilities**: The image includes utilities like curl, git, vim, zsh, gettext, nmap, and iputils-ping.
- **Zsh**: Zsh is the default shell, and oh-my-zsh (omz) is installed for additional features.
- **Powerlevel10k**: This theme for oh-my-zsh is installed for a better terminal user experience.
- **Syntax Highlighting**: zsh-syntax-highlighting plugin is installed for better command line experience.
- **multi-pltform**: Image made for both amd64 and arm64

> **IMPORTANT** Shell configuration can be done on project to project basis. Oh-my-zsh is pre-installed as well some helpful plugins
> > Because of the installation of omz there is a default omz configuration at `.zshrc,` one can change configuration by overwriting with there on `.zshrc` file

## Usage

You can use this Docker image as a base for your Python projects. It's especially useful if you prefer using zsh and oh-my-zsh in your development environment.

An entrypoint script is includedin this image for recreating and creating a requirements.txt file 