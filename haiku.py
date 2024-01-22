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
        res = {"titile": "haiku", "body": "some errors from our AI API, may be rate limit exceeded - we are working on it!"}
    return {'title': 'haiku', 'body': res.content}


@bp.route('/critique')
def critique():
    # TODO: add request method and db logic to render a reponse to user haiku
    return render_template('haiku/critique.html')

@bp.route('/response')
def response():
    res = session['response']
    return render_template('haiku/response.html', response=res)