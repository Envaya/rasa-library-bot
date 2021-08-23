# FROM registry.gitlab.com/youengineering/intern/craftcms/craft-shared/build:latest


FROM python:3.8

# install dependencies
WORKDIR /root
RUN apt-get -qq update && \
    apt-get install -qqy --no-install-recommends
RUN python -m pip install --upgrade pip==20.2


COPY requirements.txt .
RUN pip install -r requirements.txt

# install nlp model spacy
RUN pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
RUN pip install --default-timeout=1800 "https://github.com/explosion/spacy-models/releases/download/de_dep_news_trf-3.0.0/de_dep_news_trf-3.0.0-py3-none-any.whl"

# expose port for rasa server
EXPOSE 5005

# expose port for rasa X server
EXPOSE 5002

# expose port for ssh
EXPOSE 22
EXPOSE 443
EXPOSE 80

#TODO switch user to 1001