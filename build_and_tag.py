#!/usr/bin/env python3
import argparse
import subprocess

def docker_login():
    '''
    This function handles the Docker login process. It runs the "docker login" command
    and checks the return code to determine if the login was successful. If the login fails,
    it prints a message and retries the login process in a loop until a successful login is achieved.
    This is needed because if you create a new repo on docker hub you will need to login and logout to push the tags initially.
    '''
    login_success = False
    while not login_success:
        result = subprocess.run("docker login", shell=True)
        if result.returncode == 0:
            login_success = True
        else:
            print("Login failed. Please try again.")

def run_docker_commands(version):
    '''
    To run script, build_and_tag.py <input version of image here>
    After running this script you can check the images in docker desktop and push the tags to dockerhub
    This function sets up the buildx builder instance for multi-architecture builds, builds the Docker images, tags the imgaes and pushes to registry with the specified version.
    '''
    repo="python-base"
    base_image_slim = f"aliciousness/python-base:v{version}-python3.11-bookworm-slim"
    base_image_bookworm = f"aliciousness/python-base:v{version}-python3.11-bookworm"

    docker_login()

    # Create and use a new buildx builder instance with the docker-container driver
    subprocess.run(f"docker buildx create --use --name {repo} --driver docker-container", shell=True)
    subprocess.run(f"docker buildx inspect {repo} --bootstrap", shell=True)

    commands = [
        f"docker buildx build --build-arg IMAGE_VERSION={version} --platform linux/amd64,linux/arm64 -t {base_image_slim} -f 3.11/bookworm-slim/Dockerfile --push .",
        f"docker buildx imagetools create --tag aliciousness/python-base:latest {base_image_slim}",
        f"docker buildx imagetools create --tag aliciousness/python-base:python3 {base_image_slim}",
        f"docker buildx imagetools create --tag aliciousness/python-base:python3.11 {base_image_slim}",
        f"docker buildx imagetools create --tag aliciousness/python-base:v{version}-python3-slim {base_image_slim}",
        f"docker buildx imagetools create --tag aliciousness/python-base:v{version}-python3-debian {base_image_slim}",
        f"docker buildx build --build-arg IMAGE_VERSION={version} --platform linux/amd64,linux/arm64 -t {base_image_bookworm} -f 3.11/bookworm/Dockerfile --push .",
        f"docker buildx imagetools create --tag aliciousness/python-base:v{version}-python3-bookworm {base_image_bookworm}",
        f"docker buildx imagetools create --tag aliciousness/python-base:v{version}-bookworm {base_image_bookworm}"
    ]

    for command in commands:
        subprocess.run(command, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build and tag Docker images.')
    parser.add_argument('version', type=str, help='The version to use for tagging the Docker images.')

    args = parser.parse_args()

    run_docker_commands(args.version)
