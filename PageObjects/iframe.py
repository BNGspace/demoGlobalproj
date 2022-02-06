from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class ifameverify:
    testershub_by_xpath = "//a[text()='Tester’s Hub']"
    demo_testershub_by_xpath = "//a[@class='no_border sub_menu_parent']"
    iframe_by_Xpath="//a[normalize-space()='Frames']"
    search_by_xpath="//input[@type='text']"
    newwindow_by_xpath="//li[@id='Open New Window']"
    click_iframe="//li[@id='iFrame']"
    frame_switch_xpath="//iframe[@class='demo-frame lazyloaded']"

    def __init__(self,driver):
        self.driver=driver

    def iframetest(self):
        self.mainmenu = self.driver.find_element(By.XPATH, self.testershub_by_xpath)
        self.submenu = self.driver.find_element(By.XPATH, self.demo_testershub_by_xpath)
        self.Actions = ActionChains(self.driver)
        self.Actions.move_to_element(self.mainmenu).move_to_element(self.submenu).click().perform()
        self.driver.find_element(By.XPATH, self.iframe_by_Xpath).click()
        self.driver.find_element(By.XPATH, self.click_iframe).click()

    def passinput(self):
        self.mainmenu = self.driver.find_element(By.XPATH, self.search_by_xpath).send_keys("Selenium")

    def clickonNewWindow(self):
        self.driver.find_element(By.XPATH, self.newwindow_by_xpath).click()


