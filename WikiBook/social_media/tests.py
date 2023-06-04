from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DialogBoxFound(LiveServerTestCase):

    def test_register_user_error_context(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        selenium = webdriver.Chrome(options=chrome_options)

        selenium.get('http://localhost:8000/accounts/register')

        username = selenium.find_element(By.ID, 'id_username')
        email = selenium.find_element(By.ID, 'id_email')
        password1 = selenium.find_element(By.ID, 'id_password1')
        password2 = selenium.find_element(By.ID, 'id_password2')

        send_button = selenium.find_element(
            By.CSS_SELECTOR, "input[type=submit]")

        username.send_keys("hellsank")
        email.send_keys("hellsank@domain.com")
        password1.send_keys("password")
        password2.send_keys("password")

        send_button.send_keys(Keys.RETURN)

        assert "context-error" in selenium.page_source
