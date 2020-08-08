# What SCMS ?
SCMS Mean : SSL Certificate Monitoring System.
I used some Free SAAS App to monitor my Website.
Nonetheless it can't monitor my ssl certificate, so I create this little interface that monitor my certificates.

If the certicate expire under 15 days the SCMS return a 400 Code error (temporary) that trigger an alert on my dashboard and you just have to renew the certificate.

The source code is not the prettiest possible just like the front page.

# How to use it ?
Git clone the project.
Go into app directory. 
pip install -e . 

waitress-serve --call 'flaskr:create_app'
