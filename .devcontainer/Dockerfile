FROM python:3.8-slim-buster

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Ensure apt is in non-interactive to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# copy  config changes to .jupyter dir
COPY handlers.py .jupyter/handlers.py
COPY jupyter_notebook_config.py .jupyter/jupyter_notebook_config.py

# Install dependencies.
RUN apt-get -y update --no-install-recommends \
    && apt-get -y install --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    apt-utils \
    dialog \
    git \
    vim \
    && apt-get autoremove -y \
    && apt-get clean -y

# Add Node.js repository.
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -

# Install Node.js.
RUN apt-get -y update --no-install-recommends \
    && apt-get -y install --no-install-recommends nodejs \
    && apt-get autoremove -y \
    && apt-get clean -y

RUN pip install jupyterlab jupyter

# Create the user.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

ENV DEBIAN_FRONTEND=dialog

USER $USERNAME
