from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class dialogboxverify:

    testershub_by_xpath = "//a[text()='Tester’s Hub']"
    demo_testershub_by_xpath = "//a[@class='no_border sub_menu_parent']"
    dialogbox_by_xpath="//span[normalize-space()='Dialog Boxes']"
    createuser_by_xpath="//button[@id='create-user']"
    username_by_xpath="//input[@name='name']"
    email_by_xpath="//input[@name='email']"
    password_by_xpath="//input[@name='password']"
    clickbutton_by_xpath="//button[@type='button']"


    def __init__(self,driver):
        self.driver=driver


    def diglogboxdemo(self):
        self.mainmenu = self.driver.find_element(By.XPATH, self.testershub_by_xpath)
        self.submenu = self.driver.find_element(By.XPATH, self.demo_testershub_by_xpath)
        self.sub= self.driver.find_element(By.XPATH, self.dialogbox_by_xpath)
        self.Actions = ActionChains(self.driver)
        self.Actions.move_to_element(self.mainmenu).move_to_element(self.submenu).move_to_element(self.sub).click().perform()
        #self.driver.find_element(By.XPATH, self.dialogbox_by_xpath).click()


    def createuser(self):
        self.driver.find_element(By.XPATH, self.createuser_by_xpath).click()
        self.driver.find_element(By.XPATH, self.username_by_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_by_xpath).send_keys("BNG123")
        self.driver.find_element(By.XPATH, self.email_by_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_by_xpath).send_keys("BNG123@gmail.com")
        self.driver.find_element(By.XPATH, self. password_by_xpath).clear()
        self.driver.find_element(By.XPATH, self. password_by_xpath).send_keys("BNG123456")
        self.driver.find_element(By.XPATH, self. clickbutton_by_xpath).click()