FROM nwpc-oper/ploto:base

LABEL maintainer="perilalroc@gmail.com"

RUN cd /srv/ploto \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install .

WORKDIR /srv/run

ENTRYPOINT ["python3", "/srv/ploto/ploto/scheduler/rabbitmq/consumer/consumer.py"]

CMD ["--config-file=/etc/ploto/consumer.config.yaml"]