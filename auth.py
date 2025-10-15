# vulnerable auth implementation
users_db = {}


def register_user(username, password):
    
    users_db[username] = {'password': password}

def login_user(username, password):
    user = users_db.get(username)
    if not user:
        return False
    return user['password'] == password
    