import pytest

from Baseclass import BaseClass
from Homepage import Homepage


class Testcart(BaseClass):

    def test_cart(self,dataload):
        homepage = Homepage(self.driver)
        log = self.getlogger()
        self.driver.implicitly_wait(10)
        homepage.getdata1().click()
        carts = homepage.getdata2()
        log.info(f"Count is : {len(carts)}")
        print(carts[1].text)
        for cart in carts :
            if cart.find_element_by_xpath("parent::div/parent::div/div/h4").text == dataload["A"]:
                cart.click()
                break

        homepage.getdata4().click()
        homepage.getdata5().click()
        homepage.getdata6().send_keys("Ind")
        countries = homepage.getdata7()
        for country in countries :
            if country.text == 'India':
                country.click()
                break
        homepage.getdata8().click()
        assert 'Success' in homepage.getdata9().text
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")

    @pytest.fixture(params=[{'A':'Blackberry'},{'A':'iphone X'}])
    def dataload(self,request):
        return request.param

