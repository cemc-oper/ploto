FROM nwpc-oper/ploto:base

LABEL maintainer="perilalroc@gmail.com"

COPY ploto-server/ /srv/ploto-server

RUN cd /srv/ploto \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install . \
    && cd /srv/ploto-server \
    && pip install .

WORKDIR /srv/ploto-server

EXPOSE 80

ENTRYPOINT ["python3", "./run_server.py"]

CMD ["--config-file=/etc/ploto/server.config.yaml"]