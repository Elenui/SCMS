FROM "python:3.7-stretch"

MAINTAINER Alexis TARUSSIO <alexis.tarussio@gmail.com>

WORKDIR /SCMS

COPY app/* ./
RUN pip install -e .
RUN ls -ltra && sleep 10
EXPOSE 8080 
CMD ["waitress-serve", "--call", "flaskr:create_app"]