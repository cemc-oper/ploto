FROM nwpc-oper/ploto-esmdiag:base

LABEL maintainer="perilalroc@gmail.com"

USER hujk

WORKDIR /srv/run

COPY ploto/ /srv/ploto
COPY ploto-esmdiag/ /srv/ploto-esmdiag
COPY vendor/ /srv/vendor

SHELL ["conda", "run", "-n", "ncl_stable", "/bin/bash", "-c"]

RUN echo $(which python3) \
    && cd /srv/ploto \
    && python3 -m pip  config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && python3 -m pip install . \
    && cd /srv/ploto-esmdiag \
    && python3 -m pip install .

#SHELL ["/bin/bash", "-c"]
RUN echo "source activate ncl_stable" > ~/.bashrc
ENV PATH /opt/conda/envs/ncl_stable/bin:$PATH

ENTRYPOINT ["python3", "/srv/ploto/ploto/scheduler/rabbitmq/consumer/consumer.py"]

#ENV NCARG_NCARG=/usr/share/ncarg
ENV ESMDIAG_ROOT=/srv/vendor/esmdiag

CMD ["--config-file=/etc/ploto/consumer.config.yaml"]