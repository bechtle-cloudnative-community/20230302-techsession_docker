FROM ubuntu:jammy

RUN apt update && apt install -y \
python3 \
python3-pip

RUN mkdir /app

COPY ./src/requirements.txt /opt/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /opt/requirements.txt

COPY ./src /app

WORKDIR /app

EXPOSE 8000

CMD python3 api.py