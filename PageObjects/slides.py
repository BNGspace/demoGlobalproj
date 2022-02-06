import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class slidesverify:
    testershub_by_xpath = "//a[text()='Tester’s Hub']"
    demo_testershub_by_xpath = "//a[@class='no_border sub_menu_parent']"
    slides_by_xpath="//a[text()='Slider']"
    colorpicker_BY_Id="Color Picker"
    greenbutton_slider_css="div[id='green'] span[class='ui-slider-handle ui-corner-all ui-state-default']"

    def __init__(self,driver):
        self.driver=driver

    def slidesdemo(self):
        self.mainmenu = self.driver.find_element(By.XPATH, self.testershub_by_xpath)
        self.submenu = self.driver.find_element(By.XPATH, self.demo_testershub_by_xpath)
        self.Actions = ActionChains(self.driver)
        self.Actions.move_to_element(self.mainmenu).move_to_element(self.submenu).click().perform()
        self.driver.find_element(By.XPATH,self.slides_by_xpath).click()
        self.driver.find_element(By.ID, self.colorpicker_BY_Id).click()

    def performsidetesk(self):
        elem1 = self.driver.find_element(By.CSS_SELECTOR, self.greenbutton_slider_css)
        self.Actions1 = ActionChains(self.driver)
        time.sleep(5)
        self.Actions1.drag_and_drop_by_offset(elem1, 60, 0).perform()




