from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self,driver):
        self.driver=driver

    a=(By.XPATH,"//a[text()='Shop']")
    b=(By.CSS_SELECTOR,"[class='btn btn-info']")
    c=(By.XPATH,"parent::div/parent::div/div/h4")
    d=(By.CSS_SELECTOR,"[class='nav-link btn btn-primary']")
    e=(By.CSS_SELECTOR,"[class='btn btn-success']")
    f=(By.ID,"country")
    g=(By.CSS_SELECTOR,"[class='suggestions'] ul li")
    h=(By.CSS_SELECTOR,"[type = 'submit']")
    i=(By.CSS_SELECTOR,"[class='alert alert-success alert-dismissible")

    def getdata1(self):
        return self.driver.find_element(*Homepage.a)
    def getdata2(self):
        return self.driver.find_elements(*Homepage.b)
    def getdata3(self):
        return self.driver.find_element(*Homepage.c)
    def getdata4(self):
        return self.driver.find_element(*Homepage.d)
    def getdata5(self):
        return self.driver.find_element(*Homepage.e)
    def getdata6(self):
        return self.driver.find_element(*Homepage.f)
    def getdata7(self):
        return self.driver.find_elements(*Homepage.g)
    def getdata8(self):
        return self.driver.find_element(*Homepage.h)
    def getdata9(self):
        return self.driver.find_element(*Homepage.i)

