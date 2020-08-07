FROM "python:3.7-stretch"

MAINTAINER Alexis TARUSSIO <alexis.tarussio@gmail.com>

WORKDIR /PCCS
RUN apt-get update \
    && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev


COPY app/* ./

RUN pip install -e . && flask init-db
EXPOSE 8080 
CMD ["waitress-serve", "--call", "'flaskr:create_app'"]