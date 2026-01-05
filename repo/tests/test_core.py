from taskflow.core import run

def test_run_executes_tasks():
    result = []
    run([lambda: result.append(1)])
    assert result == [1]
