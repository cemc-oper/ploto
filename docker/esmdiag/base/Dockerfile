FROM continuumio/anaconda3

LABEL maintainer="perilalroc@gmail.com"

COPY docker/esmdiag/base/sources.list /etc/apt/sources.list
#COPY docker/esmdiag/base/.condarc /root/.condarc

RUN conda create -n ncl_stable -c conda-forge ncl cdo

CMD ["bash"]