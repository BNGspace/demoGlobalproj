import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from utilities.CustomLogging import Logs
from utilities.readProperties import ReadConfig
from PageObjects.dialogbox import dialogboxverify


class Test_004_Dialogbox:

    baseURL=ReadConfig.getURL()
    logger = Logs.loggen()
    frame_switch_xpath = "//iframe[@class='demo-frame lazyloaded']"

    def test_famedemo(self,setup):
        self.logger.info("************** Test_004_Dialogbox: ***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("************** Successfully opened WebPage *****")

        self.db=dialogboxverify(self.driver)
        self.db.diglogboxdemo()
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,self.frame_switch_xpath))
        self.logger.info("************** Switched to Frames ***************")
        self.logger.info("************** Creating user with name,email and Password ***************")
        self.db.createuser()
        self.logger.info("************** User Creation Completed ***************")
        self.driver.close()