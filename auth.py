# auth.py - secure version (illustrative, in-memory store only)
import os
from bcrypt import gensalt, hashpw, checkpw
from dotenv import load_dotenv

load_dotenv()

# Very small, illustrative in-memory store (do not use in production)
users_db = {}

def hash_password(plain_password: str) -> bytes:
    salt = gensalt()  # generate per-password salt
    return hashpw(plain_password.encode('utf-8'), salt)

def register_user(username: str, password: str):
    """Hashes password before storing."""
    hashed = hash_password(password)
    users_db[username] = {'password_hash': hashed}

def login_user(username: str, password: str) -> bool:
    user = users_db.get(username)
    if not user:
        return False
    return checkpw(password.encode('utf-8'), user['password_hash'])
