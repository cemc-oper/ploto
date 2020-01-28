FROM continuumio/anaconda3

LABEL maintainer="perilalroc@gmail.com"

COPY docker/esmdiag/base/sources.list /etc/apt/sources.list
#COPY docker/esmdiag/base/.condarc /root/.condarc

RUN groupadd -g 1004 hujk \
    && useradd -u 1004 -g 1004 --create-home hujk \
    && mkdir -p /srv \
    && chown -R hujk:hujk /srv \
    && chown -R hujk:hujk /opt/conda

USER hujk

RUN conda create -n ncl_stable -c conda-forge ncl cdo imagemagick

CMD ["bash"]