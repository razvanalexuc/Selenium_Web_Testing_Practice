from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class blogspotPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.ID, 'name')
        self.email_field = (By.ID, 'email')
        self.phone_field = (By.ID, 'phone')
        self.address_field = (By.ID, 'textarea')
        self.male_radio = (By.CSS_SELECTOR, 'input.form-check-input#male')
        self.search_field = (By.XPATH, '//input[@class="wikipedia-search-input" and @id="Wikipedia1_wikipedia-search-input"]')
        self.search_button = (By.XPATH, '//input[@class="wikipedia-search-button"]')
        self.arrived_search_text = (By.XPATH, '//div[contains(text(), "Search results")]')
        self.pagination = (By.ID, 'pagination')
        self.xpath_first_field = (By.ID, 'input1')
        self.xpath_second_field = (By.ID, 'input2')
        self.xpath_third_field = (By.ID, 'input3')
        self.desired_action = ActionChains(self.driver)

    def accept_cookies(self):
        try:
            cookie_banner = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cookie-choices-text'))
        )
            if cookie_banner:
                self.driver.find_element(By.ID, 'cookieChoiceDismiss').click()
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(cookie_banner))
        except:
            pass 
        
    def enter_name(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.name_field))
        self.driver.find_element(*self.name_field).send_keys(username)

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_field))
        self.driver.find_element(*self.email_field).send_keys(email)
    
    def enter_phone(self, phonenumber):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_field))
        self.driver.find_element(*self.phone_field).send_keys(phonenumber)

    def enter_address(self, address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.address_field))
        self.driver.find_element(*self.address_field).send_keys(address)
    
    def click_male(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.male_radio))
        self.driver.find_element(*self.male_radio).click()

    def select_day(self, day_name):
        self.driver.find_element(By.XPATH, f"//input[@class='form-check-input' and @id='{day_name}']").click()
    
    def select_country(self, n):
        country_name = ["usa", "canada", "uk", "germany", "france", "australia", "japan", "china", "brazil", "india"]
        self.driver.find_element(By.XPATH, f"//select[@class='form-control']//option[@value='{country_name[n]}']").click()
    
    def select_color(self, n):
        colors = ["red", "blue", "green", "yellow", "white"]
        self.driver.find_element(By.XPATH, f"//select[@class='form-control']//option[@value='{colors[n]}']")
    
    def click_element_and_go_back(self, n): # OBSOLETE - site has been updated
    #     page_options = ["open cart", "orange HRM"]
    #     self.driver.find_element(By.XPATH, f'//a[contains(text(), "{page_options[n]}")]').click()
    #     WebDriverWait(self.driver, 5).until(EC.new_window_is_opened(1))
    #     self.driver.back()
        pass
    
    def interact_with_html_static_table(self):
        rows = self.driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, "td")
            book_name = cells[0].text
            author = cells[1].text
            subject = cells[2].text
            price = cells[3].text
            print(f"Book: {book_name}, author: {author}, subject: {subject}, price: {price}")
    
    def interact_with_pagination_table(self):
        rows = self.driver.find_elements(By.XPATH, "//table[@id='productTable']//tr")
        pages = self.driver.find_elements(By.XPATH, "//ul[@class='pagination']//li")
        for i in range(len(pages)):
            pages = self.driver.find_elements(By.XPATH, "//ul[@class='pagination']//li") 
            #StaleElement was occuring because pages variable was not being relocated after each page click, so we redeclared it in the for loop
            pages[i].click()
            rows = self.driver.find_elements(By.XPATH, "//table[@id='productTable']//tr")
            #StaleElement was occuring because rows variable was not being relocated after each page click, so we redeclared it in the for loop
            for row in rows[1:]:
                cells = row.find_elements(By.TAG_NAME, "td")
                id = cells[0].text
                name = cells[1].text
                price = cells[2].text
                print(f"ID: {id}, name: {name}, price: {price}")

    def xpath_axes(self, firstinput, secondinput, thirdinput):
        self.driver.find_element(*self.xpath_first_field).send_keys(f'{firstinput}')
        self.driver.find_element(*self.xpath_second_field).send_keys(f'{secondinput}')
        self.driver.find_element(*self.xpath_third_field).send_keys(f'{thirdinput}')
    
    def search_on_wiki(self, words):
        self.driver.find_element(*self.search_field).send_keys(words)
        #WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.arrived_search_text))
        self.driver.find_element(*self.search_button).click()
    
    def interact_with_dynamic_button(self, n):
        state = ["stop", "start"] # 0 = stop, 1 = start
        self.driver.find_element(By.XPATH, f"//button[@name='{state[n]}']").click()

    def alert_handling(self, n):
        buttons = ['alertBtn', 'confirmBtn', 'promptBtn']
        identifier = self.driver.find_element(By.ID, f'{buttons[n]}')

        identifier.click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        if buttons[n] == 'alertBtn':
            alert.accept()
            print('alert was chosen')
        elif buttons[n] == 'confirmBtn':
            alert.accept()
            print('confirmation was chosen')
        elif buttons[n] == 'promptBtn':
            alert.send_keys('TEST')
            alert.accept()
            print('prompt was chosen')

    def double_clicking(self, copied_message):
        first_text_field = self.driver.find_element(By.ID, 'field1')
        first_text_field.clear()
        first_text_field.send_keys(copied_message)
        second_text_field = self.driver.find_element(By.ID, 'field2')
        copy_text_button = self.driver.find_element(By.XPATH, '//button[@ondblclick="myFunction1()"]')

        self.desired_action.double_click(copy_text_button).perform()

        if first_text_field.text == second_text_field.text:
            print("Message has been copied successfully!")
        else:
            print("Message failed to copy")

    def drag_and_drop(self):
        draggable_object = self.driver.find_element(By.XPATH, '//div[@id="draggable"]')
        desired_area = self.driver.find_element(By.XPATH, '//div[@id="droppable"]')    
        self.desired_action.drag_and_drop(draggable_object, desired_area).perform()
    
    def move_slider(self, percentage):
        slider_mover = self.driver.find_element(By.XPATH, '//span[@class="ui-slider-handle ui-corner-all ui-state-default"]')
        slider_track = self.driver.find_element(By.ID, 'slider')
        slider_width = slider_track.size['width']
        offset = slider_width * (percentage/100)
        self.desired_action.click_and_hold(slider_mover).move_by_offset(offset, 0).perform()
    
    def resizable_element(self, offset_x, offset_y):
        resizable_track = self.driver.find_element(By.XPATH, '//div[@id="resizable"]/div[contains(@class, "ui-resizable-handle")]')
        self.desired_action.click_and_hold(resizable_track).move_by_offset(offset_x, offset_y).perform()

    

class test_for_fields:
    # Configurations

    options = Options()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    blogspot_page = blogspotPage(driver=driver)
    driver.get('https://testautomationpractice.blogspot.com')
    
    # Interacting with various elements

    blogspot_page.enter_name('Razvanel')
    blogspot_page.enter_email('razvanrzv@gmail.com')
    blogspot_page.enter_phone('0701234123')
    blogspot_page.enter_address('Teilor')
    blogspot_page.click_male()
    blogspot_page.select_day('sunday')
    blogspot_page.select_country(1)
    blogspot_page.select_color(3)
    blogspot_page.click_element_and_go_back(0)
    blogspot_page.interact_with_html_static_table()
    blogspot_page.search_on_wiki('webtesting')
    blogspot_page.interact_with_dynamic_button(1)
    blogspot_page.interact_with_pagination_table()
    blogspot_page.xpath_axes('testing', 'is', 'cool')
    blogspot_page.accept_cookies() # without accepting cookies, the alert handling doesn't work
    blogspot_page.alert_handling(2)
    blogspot_page.double_clicking('testable')
    blogspot_page.drag_and_drop()
    blogspot_page.move_slider(30)
    blogspot_page.resizable_element(30, 20)
    
    time.sleep(2)
    
    driver.quit()
    
