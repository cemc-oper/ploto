FROM python:3.6

LABEL maintainer="perilalroc@gmail.com"

COPY docker/earth/base/sources.list /etc/apt/sources.list
COPY dist/app/cdo-1.9.6.tar.gz /tmp/cdo-1.9.6.tar.gz

RUN apt update \
    && apt install -y ncl-ncarg libnetcdf-dev

RUN cd /tmp \
    && tar zxvf cdo-1.9.6.tar.gz \
    && cd cdo-1.9.6 \
    && ./configure --with-netcdf=yes --with-hdf5=/usr/lib/x86_64-linux-gnu/hdf5/serial --prefix=/usr \
    && make \
    && make install \
    && cd /tmp \
    && rm -rf *.tar.gz

CMD ["bash"]