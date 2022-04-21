import pytest

@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {'stdout': '', 'write_calls': 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.tdout, 'write', fake_write)
    return buffer

@pytest.fixture(scope="session")
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn: #connection will stop after tests
        yield conn