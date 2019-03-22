FROM nwpcc/ploto-base

LABEL maintainer="perilalroc@gmail.com"

WORKDIR /srv/ploto_server

EXPOSE 80

ENTRYPOINT ["python3", "./run_server.py"]

CMD ["--config-file=/etc/ploto/server.conf.yml"]