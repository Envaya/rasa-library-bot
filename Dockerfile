# FROM registry.gitlab.com/youengineering/intern/craftcms/craft-shared/build:latest


FROM python:3.8

# install dependencies
# RUN pip install --upgrade pip==20.2
WORKDIR /root

RUN python -m pip install --upgrade pip==20.2

COPY requirements.txt .
#RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

# spacy
RUN pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
RUN pip install --default-timeout=1800 "https://github.com/explosion/spacy-models/releases/download/de_dep_news_trf-3.0.0/de_dep_news_trf-3.0.0-py3-none-any.whl"
#RUN pip install de_dep_news_trf
#RUN pip install
#RUN python -m spacy --default-timeout=10000 download de_dep_news_trf

# expose port for rasa server
EXPOSE 5005

# expose port for rasa X server
EXPOSE 5002


#VOLUME ["/ip5-auxilio-rasa"]