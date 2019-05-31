FROM python:3.6

LABEL maintainer="perilalroc@gmail.com"

COPY ploto/ /srv/ploto
COPY ploto-server/ /srv/ploto-server

RUN cd /srv/ploto \
    && pip install . \
    && cd /srv/ploto-server \
    && pip install .

WORKDIR /srv/ploto-server

EXPOSE 80

ENTRYPOINT ["python3", "./run_server.py"]

CMD ["--config-file=/etc/ploto/server.config.yaml"]