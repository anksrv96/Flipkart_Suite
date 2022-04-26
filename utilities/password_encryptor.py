from cryptography.fernet import Fernet
import bcrypt
import keyring

from utilities.password_hasher import PasswordHasher

service_id = "Credentials"
username = "ashrivastav693@gmail.com"
password = PasswordHasher.hash_password()

keyring.set_password(service_id, username, password)

#key = Fernet.generate_key()
#encrypter = Fernet(key)
#encrypted_password = encrypter.encrypt("")
