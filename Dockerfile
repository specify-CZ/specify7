FROM specifyconsortium/specify7-service:7.12.0@sha256:82bf6c49952b4d1a52c723c173b9a5258ed46b4e315f1750910073e2e741fd29
LABEL org.opencontainers.image.source=https://github.com/biodiversity-cz/specify7
LABEL description="Individual build of Specify 7 docker image"

COPY --chown=specify:specify docker-entrypoint.sh /opt/specify7/docker-entrypoint.sh
COPY --chown=specify:specify specify_settings.py /opt/specify7/settings/specify_settings.py
COPY --chown=specify:specify local_specify_settings.py /opt/specify7/settings/local_specify_settings.py


USER root
RUN mkdir /sock && \
    chown -R specify:specify /sock && \
    chmod -R 777 /volumes && \
    chmod -R 777 /sock

USER specify

#https://discourse.specifysoftware.org/t/specify-7-10-release-announcement/2196
ENV SPECIFY_CONFIG_DIR=/opt/specify7/config
CMD ["ve/bin/gunicorn", "-w", "3", "-b", "unix:/sock/docker.sock", "-t", "300", "specifyweb_wsgi"]
