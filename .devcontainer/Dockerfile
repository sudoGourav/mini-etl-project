FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install common tools
RUN apt update && apt install -y \
    git \
    curl \
    wget \
    build-essential \
    python3 \
    python3-pip \
    openjdk-17-jdk

WORKDIR /workspace