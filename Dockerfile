FROM jenkinsci/blueocean

USER root


RUN curl -L \
  "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose \
  && chmod +x /usr/local/bin/docker-compose

