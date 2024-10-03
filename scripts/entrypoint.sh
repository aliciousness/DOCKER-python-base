#!/bin/sh
# Entrypoint script to keep the container alive

# print out a reqirements.txt file for python
# Using an environment variable to check if the user wants to recreate the requirements.txt file
if [ "$RECREATE_REQUIREMENTS" = "true" ]; then
  echo "Creating requirements.txt file..."
  pip freeze > requirements.txt
  echo "requirements.txt file created."
fi

# Execute the command passed to the docker container
echo "Starting the command execution from docker-compose..."
"$@"
echo "Command execution finished, entering the loop..."

# After the command execution, keep the container alive with a loop
while true; do
  sleep infinity
done
