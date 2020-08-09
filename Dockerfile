FROM "python:3.7-stretch"

MAINTAINER Alexis TARUSSIO <alexis.tarussio@gmail.com>

WORKDIR /SCMS

COPY flaskr/ /SCMS/flaskr/
COPY requirements.txt /SCMS
COPY setup.py /SCMS 
RUN ls -ltra && sleep 10
RUN pip install -r requirements.txt
EXPOSE 8080 
CMD ["waitress-serve", "--call", "flaskr:create_app"]