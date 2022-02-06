import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from PageObjects.tabs import tabsverify
from utilities.CustomLogging import Logs
from utilities.readProperties import ReadConfig

class Test_001_Tabs:

    baseURL=ReadConfig.getURL()
    logger = Logs.loggen()

    def test_tabsdemo(self,setup):
        self.logger.info("***********Verifying Tabs Page Title *******")
        self.driver=setup
        self.driver.get(self.baseURL)


        self.tv=tabsverify(self.driver)
        self.tv.TH_to_Tab()

        pageTitle=self.driver.title
        if pageTitle=="Accordion and Tabs | QA Demo Testing Site - Global SQA":
            assert True
            self.logger.info("************** Tabs Page is Passed ******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_tabsdemo.png")
            self.driver.close()
            self.logger.error("************** Tabs Page is is Failed *****")
            assert False
