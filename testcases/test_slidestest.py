import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from utilities.CustomLogging import Logs
from utilities.readProperties import ReadConfig
from PageObjects.slides import slidesverify

class Test_003_slides:
    baseURL = ReadConfig.getURL()
    logger = Logs.loggen()
    frame_switch_xpath = "//iframe[@class='demo-frame lazyloaded']"
    def test_clickonslides(self,setup):
        self.logger.info("************** Test_003_Slides Testase **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("************** Successfully opened WebPage ******")

        self.sv=slidesverify(self.driver)
        self.logger.info("************** Testing Slides Concept ***********")
        self.sv.slidesdemo()
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,self.frame_switch_xpath))

        self.logger.info("************** Switched to Frames ****************")
        self.logger.info("************** Started Slides Task ***************")

        self.sv.performsidetesk()
        self.logger.info("************** Slides Task Completed *************")
        self.driver.close()



