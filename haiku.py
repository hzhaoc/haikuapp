from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
# from werkzeug.exceptions import abort
from haiku.db import get_db
from . import llm, err, db


bp = Blueprint('haiku', __name__)


@bp.route('/')
def index():
    return critique()


# the page to generate haiku from ai
@bp.route('/generate', methods=('GET','POST'))
def generate():
    if request.method == 'POST':
        res = llm.invoke("generate a random haiku")
        res = {'title': 'haiku', 'body': res}
        session['response'] = res
        return redirect(url_for('haiku.response'))
    return render_template('haiku/generate.html')


# the page to enter user haiku to get ai response
@bp.route('/critique', methods=('GET','POST'))
def critique():
    if request.method == 'POST':
        haiku = request.form['body']
        res = _critique(haiku)
        session['response'] = res
        return redirect(url_for('haiku.response'))
    return render_template('haiku/critique.html')

# get formatted critique response
def _critique(haiku):
    if haiku is None:
        flash('cannot have null haiku')
    if len(haiku) == 0:
        flash('cannot have empty haiku')
    prefix = "comment on this haiku: "
    res = llm.invoke(prefix + haiku)
    db.commit_haiku(res)
    return {'title': 'reponse to haiku', 'body': res}

# the page for response, either ai haiku, or ai resposne to user haiku
@bp.route('/response')
def response():
    res = session['response']
    error = None
    if res == None:
        error = "no response"
    if error != None:
        flash(error)
        return
    return render_template('haiku/response.html', response=res)