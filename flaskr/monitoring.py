from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import datetime
import logging
import socket
import ssl
import OpenSSL
#test
bp = Blueprint('monitoring', __name__)

@bp.route('/')
def index():
    db = get_db()
    websites = {}
    status_url = True

    for website in db.execute('SELECT web_url FROM websites').fetchall(): 
        ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=website[0],
        )
        conn.connect((website[0], 443))
        ssl_info = conn.getpeercert()
        # parse the string from the certificate into a Python datetime object
        res = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        dayremaining = res - datetime.datetime.utcnow()
        if dayremaining < datetime.timedelta(days=15):
            status_url = False
            websites[website[0]] =  "alert"
        elif dayremaining < datetime.timedelta(days=30):
            websites[website[0]] =  "warning"
        else: 
            websites[website[0]] = "success"
            
    if status_url:
        return render_template('monitoring/index.html', websites=websites)
    else:
        return render_template('monitoring/index.html', websites=websites), 400


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        web_url = request.form['web_url']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO websites (web_url)'
                ' VALUES (?)',
                ((web_url,))
            )
            db.commit()
            return redirect(url_for('monitoring.index'))

    return render_template('monitoring/create.html')

