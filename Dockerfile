ARG BASE_CONTAINER=jupyter/base-notebook:python-3.8.8
FROM $BASE_CONTAINER

WORKDIR /workshop/

USER root

COPY ./deep_learning ./deep_learning
COPY ./interview_mythbusting ./interview_mythbusting
COPY ./machine_learning_foundations ./machine_learning_foundations
COPY ./mlops ./mlops
COPY ./stats_workshop ./stats_workshop
COPY ./jupyter_notebook_config.py ./
COPY ./requirements.txt ./

RUN mv ./jupyter_notebook_config.py ~/.jupyter/jupyter_notebook_config.py
RUN pip install -r ./requirements.txt
