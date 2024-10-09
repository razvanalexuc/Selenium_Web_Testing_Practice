from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, "//input[@type='text']")
        self.password_field = (By.XPATH, "//input[@type='password']")
        self.login_button = (By.XPATH, "//input[@type='submit']")

    def enter_username(self, username):
        print(f"Finding element with locator: {self.username_field}")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_field))
        self.driver.find_element(self.username_field).send_keys(username)
    
    def enter_password(self, password):
        print(f"Finding element with locator: {self.password_field}")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_field))
        self.driver.find_element(self.password_field).send_keys(password)

    def press_button(self):
        print(f"Finding element with locator: {self.login_button}")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        self.driver.find_element(self.login_button).click()

class test_LoginPage:
    # Configurations
    options = Options()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get('https://moodle2.usv.ro/login/index.php')

    # Interacting with the Login Page

    login_page = LoginPage(driver=driver)
    login_page.enter_username('studentemail')
    time.sleep(3)
    login_page.enter_password('studentpassword')
    time.sleep(3)
    login_page.press_button()
    time.sleep(3)

    driver.quit()

