import keyring
from selenium.webdriver.chrome.service import Service


class TestData:
    CHROME_EXECUTABLE_PATH = Service("/Users/ankshrivastav/PycharmProjects/Flipkart_Suite/drivers/chromedriver")
    BASE_URL = "https://www.flipkart.com/"
    SERVICE_ID = "Credentials"
    USERNAME = "ashrivastav693@gmail.com"
    PASSWORD = keyring.get_password(SERVICE_ID, USERNAME)

    LOGIN_PAGE_HEADER = "Login"

    SEARCH_QUERY = "Besan"
