FROM python:3.6

LABEL maintainer="perilalroc@gmail.com"

COPY ploto/ /srv/ploto
COPY setup.py /srv/setup.py
COPY ploto_server /srv/ploto_server
COPY vendor/ /srv/vencor

RUN cd /srv \
    && pip install .

CMD ["bash"]
