import sqlite3

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# initalize db and make it CLI
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def commit_haiku(haiku):
    # if error, raise appropriate db error in the backend
    #           and 500 internal server error to user 
    # TODO: add try-except logic to flush the db error to service log 
    #       without blocking client experience
    db = get_db()
    db.execute(
        'INSERT INTO haiku (body)'
        ' VALUES (?)',
        (haiku,)
    )
    db.commit()