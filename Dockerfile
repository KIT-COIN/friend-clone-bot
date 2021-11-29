FROM python:3.6

RUN mkdir src
COPY . src/

RUN apt-get update \
    && apt-get install -y mecab \
    && apt-get install -y mecab-ipadic \
    && apt-get install -y libmecab-dev \
    && apt-get install -y mecab-ipadic-utf8 \
    && apt-get install -y swig

RUN pip install -r ./src/requirements.txt

WORKDIR ./src/
ENTRYPOINT ["python", "main.py"]
