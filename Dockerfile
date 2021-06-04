ARG BASE_CONTAINER=jupyter/base-notebook:python-3.8.8
FROM $BASE_CONTAINER

WORKDIR /workshop/

USER root

ADD ./machine_learning_foundations/requirements.txt ./machine_learning_foundations/requirements.txt
ADD ./stats_workshop/requirements.txt ./stats_workshop/requirements.txt
ADD ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
