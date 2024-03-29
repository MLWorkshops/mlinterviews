# Preparing for the Data Science and Machine Learning Job Interview

## Chat room

The following Gitter chatroom will be monitored during the workshop and everyone is encouraged to continue the conversation in this Gitter community.

[![Gitter](https://badges.gitter.im/MLWorkshops/spring-2021-mlworkshop.svg)](https://gitter.im/MLWorkshops/spring-2021-mlworkshop?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## How to use this repository

The following decribes the contents of the repository, agenda and how to start using the notebooks.

> Note: The workshop will use Python 3.6+ and Jupyter.

### Organization

| Folder | Description |
| --- | --- |
| `data` | Instructions on getting the data for the workshop |
| `stats_workshop` | Introduction to statistical thinking |
| `machine_learning_foundations` | ML foundations and classicial ML |
| `interview_mythbusting` | Interviewing myths and truths |
| `deep_learning` | Introduction to deep learning |
| `mlops` | ML models in production |

### Agenda

[TBD]

### Getting started

#### Running Jupyter directly on a local (host) machine

- Install Python 3.6+.
- Clone the repository and `cd` into the repository.

    ```
    git clone https://github.com/MLWorkshops/mlinterviews.git
    cd mlinterviews
    ```

- Install the required Python packages with the included requirements file.

    ```
    pip install -r requirements.txt
    ```

- Start the Jupyter notebook server (option 1) or Jupyter Lab (option 2) in the same folder as the repository.

    - Starting Juypter notebooks:

    ```
    jupyter notebook
    ```

    - Starting Jupyter Lab:

    ```
    jupyter lab
    ```

#### Running Jupyter inside a docker container

- Install docker ([Docker for Mac](https://docs.docker.com/docker-for-mac/install/))
- Clone the repository and `cd` into the repository.

    ```
    git clone https://github.com/MLWorkshops/mlinterviews.git
    cd mlinterviews
    ```

- Pull the docker image from dockerhub

    ```
    make pull
    make docker-run
    ```
- Open in your browser the following link `http://127.0.0.1:8888/?token=<.....>` printed out in your terminal.
> Note: If no link with a token is printed out in your terminal, then
> open this link `http://127.0.0.1:8888/` in your browser.  

