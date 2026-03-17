import sqlite3
import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        # get_db should return the same connection each time it's called
        assert db is get_db()

    # after the context, the connection should be closed
    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)


def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    # replace the init_db function with the fake one
    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    # invoke the init-db command
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    # check that the fake init_db function was called
    assert Recorder.called
