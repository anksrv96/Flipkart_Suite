import bcrypt


class PasswordHasher:
    def hash_password(self):
        password = b"Pass@1234"
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed
