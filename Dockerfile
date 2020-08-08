FROM "python:3.7-stretch"

MAINTAINER Alexis TARUSSIO <alexis.tarussio@gmail.com>

WORKDIR /SCMS

COPY app/* ./

RUN pip install -e .
EXPOSE 8080 
CMD ["waitress-serve", "--call", "flaskr:create_app"]