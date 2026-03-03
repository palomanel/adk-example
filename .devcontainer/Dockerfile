# Ubuntu base image
FROM ubuntu:25.10

# Prevent prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive
# Set locale settings
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install Python, GCP CLI, and other devtools and dependencies
RUN apt-get update \
    && apt-get upgrade -yqq \
    && apt-get install -yqq \
        locales \
        python3 \
        python3-pip \
        python3-venv \
        curl \
        gnupg \
        lsb-release \
        ca-certificates \
        git

# Set Python 3 as the default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Install Google Cloud SDK (gcloud CLI)
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
        | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
        | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \
    && apt-get update -yqq \
    && apt-get install google-cloud-cli -yqq

# Create a non-root user for VS Code remote
RUN useradd --create-home --shell /bin/bash vscode

# Switch to the vscode user by default
USER vscode
