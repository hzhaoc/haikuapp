from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from haiku.auth import login_required
from haiku.db import get_db
from . import llm
from flask import session


bp = Blueprint('haiku', __name__)


@bp.route('/')
def index():
    return critique()


# the page to generate haiku from ai
@bp.route('/generate', methods=('GET','POST'))
def generate():
    if request.method == 'POST':
        res = _generate()
        session['response'] = res
        return redirect(url_for('haiku.response'))
    return render_template('haiku/generate.html')


# generate haiku from llm
def _generate():
    try:
        res = llm.llm_openai.invoke("generate a haiku")
    except:
        error = "some errors from our AI API, may be rate limit exceeded - we are working on it!"
        flash(error)
    return {'title': 'haiku', 'body': res.content}


# the page to enter user haiku to get ai response
@bp.route('/critique', methods=('GET','POST'))
def critique():
    # TODO: add request method  to render a reponse to user haiku
    # TODO: save user haiku to db
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
    try:
        res = llm.llm_openai.invoke(prefix + haiku)
    except:
        error = "some errors from our AI API, may be rate limit exceeded - we are working on it!"
        flash(error)
    return {'title': 'haiku', 'body': res.content}


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