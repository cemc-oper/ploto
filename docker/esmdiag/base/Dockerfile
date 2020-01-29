FROM continuumio/miniconda

LABEL maintainer="perilalroc@gmail.com"

RUN groupadd -g 1004 hujk \
    && useradd -u 1004 -g 1004 --create-home hujk \
    && mkdir -p /srv \
    && chown -R hujk:hujk /srv \
    && chown -R hujk:hujk /opt/conda

#COPY docker/esmdiag/base/.condarc /home/hujk/.condarc

USER hujk

RUN conda create -n ncl_stable -c conda-forge ncl cdo imagemagick \
    && conda clean -y -a

CMD ["bash"]