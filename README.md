# Docker-python-base
[![Docker Pulls](https://img.shields.io/badge/Docker%20Pulls-381-blue)](https://hub.docker.com/r/aliciousness/python-base)
[![Latest Release](https://img.shields.io/badge/release-v0.3.4-brightgreen)](https://github.com/aliciousness/ACTION-latest-release-badge/releases)
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/aliciousness)
<!-- [![Docker Image Size (tag)]() -->
<!-- ![Build Status](https://img.shields.io/github/actions/workflow/status/aliciousness/python-base/release.yml?branch=main)]
[![GitHub last commit](https://img.shields.io/badge/Last%20Commit-2024-11-08-yellow)] -->

This Docker image is based on Python 3.12. It's designed to provide a development environment with a set of utilities and configurations.

[Docker hub]

# Supported tags and respective Dockerfile links

- [`v0.2.4-3.12-bookworm-slim-python`, `v0.2.4-python3-debian`, `v0.2.4-slim`, `latest`, `python`]

- [`v0.2.4-python3.12-bookworm`, `v0.2.4-python3-bookworm`,`v0.2.4-bookworm`]

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