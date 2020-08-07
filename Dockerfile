FROM "python:3.7-stretch"

MAINTAINER Alexis TARUSSIO <alexis.tarussio@gmail.com>

WORKDIR /PCCS

COPY app/* ./

RUN pip install -e . && ls -la && sleep 10 && flask init-db
EXPOSE 8080 
CMD ["waitress-serve", "--call", "'flaskr:create_app'"]