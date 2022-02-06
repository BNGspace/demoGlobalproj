import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from utilities.CustomLogging import Logs
from utilities.readProperties import ReadConfig
from PageObjects.iframe import ifameverify

class Test_002_iFrame:

    baseURL=ReadConfig.getURL()
    logger = Logs.loggen()


    def test_famedemo(self,setup):
        self.logger.info("************** Test_002_Iframe ***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("************** Successfully opened WebPage *****")


        self.frm=ifameverify(self.driver)
        self.logger.info("************** Testing Frames Concept ***********")
        self.frm.iframetest()
        self.driver.switch_to.frame("globalSqa")
        self.logger.info("************** Switched to Frames ***************")
        time.sleep(5)
        self.frm.passinput()
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.logger.info("************** Coming out from Frames ************")
        self.frm.clickonNewWindow()
        self.logger.info("************** Successfully tested Frames ********")
        self.driver.close()

