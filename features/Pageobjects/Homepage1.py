from selenium.webdriver.common.by import By


class Homepage1:
    def __init__(self,driver):
        self.driver=driver

    a=(By.NAME,"name")
    b=(By.NAME,"email")
    c=(By.CSS_SELECTOR,"[type='submit']")
    d=(By.CSS_SELECTOR,"[class='alert alert-success alert-dismissible']")

    def getdata1(self):
        return self.driver.find_element(*Homepage1.a)
    def getdata2(self):
        return self.driver.find_elements(*Homepage1.b)
    def getdata3(self):
        return self.driver.find_element(*Homepage1.c)
    def getdata4(self):
        return self.driver.find_element(*Homepage1.d)



