from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Registration:
    click_register_menu_xpath = (By.XPATH, "//a[@class='ico-register']")
    text_first_name_Id = (By.ID, "FirstName")
    text_last_name_Id = (By.ID, "LastName")
    text_email_Id = (By.ID, "Email")
    text_company_name_Id = (By.ID, "Company")
    click_on_newsletter_Id = (By.ID, "Newsletter")
    text_password_xpath = (By.XPATH, "//input[@id='Password']")
    text_confirm_password_xpath = (By.XPATH, "//input[@id='ConfirmPassword']")
    click_on_register_btn_xpath = (By.XPATH, "//button[@id='register-button']")
    verify_register_page_xpath = (By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]")

    def __init__(self, driver):
        self.driver = driver

    def Click_register_menu(self):
        time.sleep(2)
        self.driver.find_element(*Registration.click_register_menu_xpath).click()

    def getGender(self, gender):
        time.sleep(2)
        if gender == "male":
            self.driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
        elif gender == "female":
            self.driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
        else:
            self.driver.find_element(By.XPATH, "//input[@id='gender-male']").click()

    def Enter_firstname(self, firstname):
        self.driver.find_element(*Registration.text_first_name_Id).clear()
        self.driver.find_element(*Registration.text_first_name_Id).send_keys(firstname)

    def Enter_lastname(self, lastname):
        self.driver.find_element(*Registration.text_last_name_Id).clear()
        self.driver.find_element(*Registration.text_last_name_Id).send_keys(lastname)

    def getDay(self, text):
        element = self.driver.find_element(By.XPATH, "//select[@name='DateOfBirthDay']")
        select = Select(element)
        select.select_by_visible_text(text)

    def getMonth(self, text):
        element = self.driver.find_element(By.XPATH, "//select[@name='DateOfBirthMonth']")
        select = Select(element)
        select.select_by_visible_text(text)

    def getYear(self, text):
        element = self.driver.find_element(By.XPATH, "//select[@name='DateOfBirthYear']")
        select = Select(element)
        select.select_by_visible_text(text)

    def Enter_email(self, email):
        self.driver.find_element(*Registration.text_email_Id).clear()
        self.driver.find_element(*Registration.text_email_Id).send_keys(email)

    def Enter_company_name(self, company_name):
        self.driver.find_element(*Registration.text_company_name_Id).clear()
        self.driver.find_element(*Registration.text_company_name_Id).send_keys(company_name)

    def Click_newsletter(self):
        self.driver.find_element(*Registration.click_on_newsletter_Id).click()

    def Enter_password(self, password):
        self.driver.find_element(*Registration.text_password_xpath).clear()
        self.driver.find_element(*Registration.text_password_xpath).send_keys(password)

    def Enter_confirm_password(self, confirm_password):
        self.driver.find_element(*Registration.text_confirm_password_xpath).clear()
        self.driver.find_element(*Registration.text_confirm_password_xpath).send_keys(confirm_password)

    def Click_register_btn(self):
        self.driver.find_element(*Registration.click_on_register_btn_xpath).click()

    def verify_register_page(self):
        expected_url = "https://demo.nopcommerce.com/registerresult/1?returnUrl=/"
        if self.driver.current_url == expected_url:
            return True
        else:
            return False

    # def generate_email_with_time_stamp(self):
    #     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    #     return "rajeshnimje" + time_stamp + "@gmail.com"
