FROM specifyconsortium/specify7-service:7.11@sha256:ae2458777a09047c4f4d24234d9f3cae1389a9e74162ba90abe6d8436edc8490
LABEL org.opencontainers.image.source=https://github.com/biodiversity-cz/specify7
LABEL description="Individual build of Specify 7 docker image"

COPY --chown=specify:specify docker-entrypoint.sh /opt/specify7/docker-entrypoint.sh
COPY --chown=specify:specify specify_settings.py /opt/specify7/settings/specify_settings.py


USER root
RUN mkdir /sock && \
    chown -R specify:specify /sock && \
    chmod -R 777 /volumes && \
    chmod -R 777 /sock

USER specify

#https://discourse.specifysoftware.org/t/specify-7-10-release-announcement/2196
ENV SPECIFY_CONFIG_DIR=/opt/specify7/config
CMD ["ve/bin/gunicorn", "-w", "3", "-b", "unix:/sock/docker.sock", "-t", "300", "specifyweb_wsgi"]
