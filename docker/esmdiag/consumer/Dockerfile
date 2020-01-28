FROM nwpc-oper/ploto-esmdiag:base

LABEL maintainer="perilalroc@gmail.com"

WORKDIR /srv/run

COPY ploto/ /srv/ploto
COPY ploto-esmdiag/ /srv/ploto-esmdiag
COPY vendor/ /srv/vendor

SHELL ["conda", "run", "-n", "ncl_stable", "/bin/bash", "-c"]

RUN groupadd -g 1004 hujk \
    && useradd -u 1004 -g 1004 --create-home hujk \
    && cd /srv/ploto \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install . \
    && cd /srv/ploto-esmdiag \
    && pip install . \
    && chmod -R a+rw /opt/conda/envs/ncl_stable /srv


ENTRYPOINT ["conda", "run", "-n", "ncl_stable", "python3", "/srv/ploto/ploto/scheduler/rabbitmq/consumer/consumer.py"]

#ENV NCARG_NCARG=/usr/share/ncarg
ENV ESMDIAG_ROOT=/srv/vendor/esmdiag

CMD ["--config-file=/etc/ploto/consumer.config.yaml"]