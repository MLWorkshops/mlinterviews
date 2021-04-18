ARG BASE_CONTAINER=jupyter/base-notebook:python-3.8.8
FROM $BASE_CONTAINER

WORKDIR /stats_workshop/

USER root

COPY . .

RUN mv ./jupyter_notebook_config.py ~/.jupyter/jupyter_notebook_config.py
RUN pip install -r ./requirements.txt
