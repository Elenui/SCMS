from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('monitoring', __name__)

@bp.route('/')
def index():
    db = get_db()
    websites = db.execute(
        'SELECT web_url'
        ' FROM websites'
    ).fetchall()

    for website in db.execute('SELECT web_url FROM websites'): 
        print(website)

    return render_template('monitoring/index.html', websites=websites)



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

