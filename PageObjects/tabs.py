from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class tabsverify:

    testershub_by_xpath = "//a[text()='Tester’s Hub']"
    demo_testershub_by_xpath = "//a[@class='no_border sub_menu_parent']"
    tabs_by_xpath = "//li[@id='menu-item-2835']//a"


    def __init__(self,driver):
        self.driver=driver

    def TH_to_Tab(self):
        self.mainmenu=self.driver.find_element(By.XPATH,self.testershub_by_xpath)
        self.submenu = self.driver.find_element(By.XPATH,self.demo_testershub_by_xpath)
        self.submenu2=self.driver.find_element(By.XPATH, self.tabs_by_xpath)
        self.Actions=ActionChains(self.driver)
        self.Actions.move_to_element(self.mainmenu).move_to_element(self.submenu).move_to_element(self.submenu2).click().perform()




