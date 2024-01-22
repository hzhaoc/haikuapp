from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from haiku.auth import login_required
from haiku.db import get_db


bp = Blueprint('haiku', __name__)


@bp.route('/')
def index():
    return critique()

@bp.route('/generate')
def generate():
    # TODO: add request method and db logic to render an AI haiku
    return render_template('haiku/generate.html')

@bp.route('/critique')
def critique():
    # TODO: add request method and db logic to render a reponse to user haiku
    return render_template('haiku/critique.html')