from taskflow.storage import save, load_all

def test_storage():
    save(1)
    assert 1 in load_all()
