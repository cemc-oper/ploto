FROM nwpcc/ploto-earth:base

LABEL maintainer="perilalroc@gmail.com"

WORKDIR /srv/run

COPY ploto/ /srv/ploto
COPY vendor/ /srv/vendor

RUN cd /srv/ploto \
    && pip install . \
    && pip install .[earth]

ENTRYPOINT ["python3", "/srv/ploto/ploto/scheduler/rabbitmq/consumer/consumer.py"]

ENV NCARG_ROOT=/usr/share/ncarg

CMD ["--config-file=/etc/ploto/consumer.config.yaml"]