FROM "python:3.7-stretch"

MAINTAINER Alexis TARUSSIO <alexis.tarussio@gmail.com>

WORKDIR /SCMS

COPY flaskr /SCMS
COPY requirements.txt /SCMS
COPY setup.py /SCMS 
RUN pip install -r requirements.txt
RUN ls -ltra && sleep 10
EXPOSE 8080 
CMD ["waitress-serve", "--call", "flaskr:create_app"]