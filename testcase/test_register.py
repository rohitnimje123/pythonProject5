import pytest
import time

from pageObject.register import Registration
from utilities import XLutils
from utilities.Logger import LogGen
from utilities.readConfigfile import ReadConfig


class Test_Registration:
    log = LogGen.loggen()
    # url = ReadConfig.geturl()
    path = "C:\\Users\\HP\\PycharmProjects\\pythonProject5\\testdata\\NopCom.xlsx"

    def test_register_001(self, setup):
        self.driver = setup
        self.driver.get("https://demo.nopcommerce.com/")
        time.sleep(4)
        self.log.info("Going to Url")
        self.rg = Registration(self.driver)
        self.rg.Click_register_menu()
        time.sleep(2)
        self.log.info("Open Register Menu")

        self.rows = XLutils.rowcount(self.path, "Sheet1")
        print("Number of rows-->", self.rows)
        time.sleep(2)
        status_list = []
        for r in range(2, self.rows + 1):
            self.firstname = XLutils.readdata(self.path, "Sheet1", r, 1)
            self.lastname = XLutils.readdata(self.path, "Sheet1", r, 2)
            self.email = XLutils.readdata(self.path, "Sheet1", r, 3)
            self.company_name = XLutils.readdata(self.path, "Sheet1", r, 4)
            self.password = XLutils.readdata(self.path, "Sheet1", r, 5)
            self.confirm_pass = XLutils.readdata(self.path, "Sheet1", r, 6)
            self.driver.implicitly_wait(3)
            self.rg.getGender("male")
            self.log.info("click on male Radio btn")
            self.rg.Enter_firstname(self.firstname)
            self.log.info("Enter firstname -->" + self.firstname)
            self.rg.Enter_lastname(self.lastname)
            self.log.info("Enter lastname -->" + self.lastname)
            self.rg.getDay("28")
            self.log.info("Enter day")
            time.sleep(2)
            self.rg.getMonth("December")
            self.log.info("Enter month")
            time.sleep(2)
            self.rg.getYear("1994")
            self.log.info("Enter year")
            self.rg.Enter_email(self.email)
            self.log.info("Enter email -->" + self.email)
            self.rg.Enter_company_name(self.company_name)
            self.log.info("Enter company name -->" + self.company_name)
            self.rg.Click_newsletter()
            self.log.info("Click on newsletter box")
            self.rg.Enter_password(self.password)
            self.log.info("Enter password -->" + self.password)
            self.rg.Enter_confirm_password(self.confirm_pass)
            self.log.info("Enter confirm pass -->" + self.confirm_pass)
            self.rg.Click_register_btn()
            self.log.info("Click on register btn")
            time.sleep(2)
            if self.rg.verify_register_page() == True:
                status_list.append("pass")
                self.driver.back()
                # XLutils.writedata(self.path, "Sheet1", r, 7, "pass")

            else:
                status_list.append("fail")
                # XLutils.writedata(self.path, "Sheet1", r, 7, "fail")
                self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\pythonProject5\\Screenshot"
                                            "\\nopCom_fail_ss.png")
            self.driver.implicitly_wait(2)
        print(status_list)
        self.driver.close()
