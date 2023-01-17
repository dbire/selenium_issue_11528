FROM python:3.10-slim-buster

ARG DEBIAN_FRONTEND=noninteractive
RUN set -x \
    && echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
	&& apt-get update \
    && apt-get install -y --no-install-recommends \
        netcat \
        git \
    \
    # clean apt packages
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

RUN pip install --upgrade pip
ADD ./requirements.txt /app/requirements_docker.txt
RUN pip install -r /app/requirements_docker.txt

COPY ./*.sh /usr/local/bin/
RUN set -x \
    && chmod +x /usr/local/bin/*.sh

WORKDIR /app
ENTRYPOINT [ "/usr/local/bin/entry_point.sh" ]