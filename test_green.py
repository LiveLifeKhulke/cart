import time

import pytest
from selenium.webdriver.support.select import Select

from Baseclass import Baseclass


class TestCase(Baseclass):

    def test_green(self,dataload):
        log = self.log()
        self.driver.implicitly_wait(6)
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.find_element_by_css_selector("[type='search']").send_keys(dataload["a"])
        time.sleep(5)
        carts=self.driver.find_elements_by_xpath("//button[text()='ADD TO CART']")
        print(len(carts))
        for cart in carts:
            if cart.find_element_by_xpath("parent::div/parent::div/h4").text == dataload["b"]:
                cart.click()
                log.info(dataload["b"])
                cart.screenshot("cart.png")
                break
        self.driver.find_element_by_css_selector("[class ='cart-icon']").click()
        self.driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
        amounts=self.driver.find_elements_by_xpath("//tr/td[5]/p")
        sum = 0
        for amount in amounts:
            sum+=int(amount.text)
        print(sum)
        self.driver.find_element_by_xpath("//button[text()='Place Order']").click()
        dropdown = Select(self.driver.find_element_by_xpath("//div/div/div/select"))
        dropdown.select_by_value("India")
        self.driver.find_element_by_css_selector("[type='checkbox']").click()
        self.driver.find_element_by_css_selector("[type='checkbox']").is_selected()
        print(self.driver.find_element_by_xpath("//button[text()='Proceed']").value_of_css_property("color"))
        self.driver.find_element_by_xpath("//button[text()='Proceed']").click()



    @pytest.fixture(params=[{'a':'br','b':'Brocolli - 1 Kg'},{'a':'gr','b':'Grapes - 1 Kg'}])
    def dataload(self,request):
        return request.param