FROM nwpcc/ploto-base

LABEL maintainer="perilalroc@gmail.com"

WORKDIR /srv/run

ENTRYPOINT ["python3", "/srv/ploto/scheduler/rabbitmq/consumer/consumer.py"]

CMD ["--config-file=/etc/ploto/consumer.conf.yml"]