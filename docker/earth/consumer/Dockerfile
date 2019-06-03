FROM nwpcc/ploto-earth:base

LABEL maintainer="perilalroc@gmail.com"

WORKDIR /srv/run

COPY ploto/ /srv/ploto
COPY vendor/ /srv/vendor

RUN groupadd -g 1004 hujk \
    && useradd -u 1004 -g 1004 --create-home hujk \
    && cd /srv/ploto \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install . \
    && pip install .[earth]

ENTRYPOINT ["python3", "/srv/ploto/ploto/scheduler/rabbitmq/consumer/consumer.py"]

ENV NCARG_NCARG=/usr/share/ncarg
ENV ESMDIAG_ROOT=/srv/vendor/esmdiag

CMD ["--config-file=/etc/ploto/consumer.config.yaml"]