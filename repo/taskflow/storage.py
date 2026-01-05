_STORE = []

def save(task):
    _STORE.append(task)

def load_all():
    return list(_STORE)
