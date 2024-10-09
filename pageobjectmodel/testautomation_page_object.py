from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait

class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, "//input[@type='text']")
        self.password_field = (By.XPATH, "//input[@type='password']")
        self.submit_button = (By.ID, 'submit')
        self.logout_button = (By.XPATH, "//a[contains(text(), 'Log out')]")
        self.error_text = (By.ID, "error")
    
    def enter_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.username_field))
        self.driver.find_element(*self.username_field).send_keys(username)
    
    def enter_password(self, password):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.password_field))
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.submit_button))
        self.driver.find_element(*self.submit_button).click()

# Test case 1: Positive login test
class test_positive_Login_page:
    options = Options()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    login_page = Loginpage(driver=driver)

    driver.get('https://practicetestautomation.com/practice-test-login/')
    login_page.enter_username('student')
    login_page.enter_password('Password123')
    login_page.click_button()
    
    WebDriverWait(driver, 5).until(EC.url_contains('practicetestautomation.com/logged-in-successfully/'))
    assert 'practicetestautomation.com/logged-in-successfully/' in driver.current_url, "URL invalid" 
    
    page_source = driver.page_source

    assert 'Congratulations' in page_source or 'successfully logged in' in page_source, "Expected message not given"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_page.logout_button))
    assert driver.find_element(*login_page.logout_button).is_displayed(), "logout button not found"

    driver.quit()
    
# Test case 2: Negative user login test
class test_negative_user_Login_page:
    options = Options()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    login_page = Loginpage(driver=driver)

    driver.get('https://practicetestautomation.com/practice-test-login/')
    login_page.enter_username('incorrectUser')
    login_page.enter_password('Password123')
    login_page.click_button()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_page.error_text))
    assert driver.find_element(*login_page.error_text).is_displayed(), 'username error text not shown'
    error_element = driver.find_element(*login_page.error_text)
    assert error_element.text == "Your username is invalid!"

    driver.quit()

# Test case 3: Negative password login test
class test_negative_password_Login_page:
    options = Options()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    login_page = Loginpage(driver=driver)
    driver.get('https://practicetestautomation.com/practice-test-login/')
    login_page.enter_username('student')
    login_page.enter_password('incorrectPassword')
    login_page.click_button()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_page.error_text))
    assert driver.find_element(*login_page.error_text).is_displayed(), 'password error text not shown'
    error_element = driver.find_element(*login_page.error_text)
    assert error_element.text == 'Your password is invalid!'

    driver.quit()


    