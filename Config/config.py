import keyring

class TestData:
    BASE_URL = "https://www.flipkart.com/"
    SERVICE_ID = "Credentials"
    USERNAME = "ashrivastav693@gmail.com"
    PASSWORD = keyring.get_password(SERVICE_ID, USERNAME)
