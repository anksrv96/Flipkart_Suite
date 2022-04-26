import bcrypt


class PasswordHasher:
    def hash_password(self):
        password = b""
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed
