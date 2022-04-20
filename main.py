import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path='c:\\geckodriver.exe')
driver.implicitly_wait(6)
driver.get("https://www.flipkart.com/")
driver.find_element_by_css_selector("[class='_2IX_2- VJZDxU']").send_keys("8851525701")
driver.find_element_by_css_selector("[type='password']").send_keys("Breaking1!")
driver.find_element_by_css_selector("[class='_2KpZ6l _2HKlqd _3AWRsL']").click()
time.sleep(3)
# driver.find_element_by_css_selector("[name='q']").send_keys("t shirts")
# driver.find_element_by_css_selector("[type='submit']").click()
# carts = driver.find_elements_by_css_selector("[class='_1xHGtK _373qXS']")
# print(len(carts))
# for cart in carts:
#     if driver.find_element_by_xpath("//a[text()='Solid Men Round Neck Multicolor T-Shirt']").text == 'Solid Men Round Neck Multicolor T-Shirt':
#         cart.click()
#         break
#
# window = driver.window_handles[1]
# driver.switch_to.window(window)
# driver.find_element_by_xpath("//a[text()='M']").click()
# driver.find_element_by_css_selector("[class = '_2KpZ6l _2U9uOA ihZ75k _3AWRsL']").click()
# driver.find_element_by_css_selector("[class = 'E3folB']").click()
# radiobutton=driver.find_elements_by_css_selector("[class='_1XFPmK']")
# radiobutton[3].click()
# time.sleep(4)
# driver.find_element_by_css_selector("[class='_2KpZ6l RLM7ES _3AWRsL']").click()
# driver.find_element_by_xpath("//button[text()='CONTINUE']").click()
# time.sleep(4)
# # [class='_1XFPmK']
# radiobutton1=driver.find_elements_by_css_selector("[class='_1XFPmK']")
# radiobutton1[2].click()
# time.sleep(4)
# driver.find_element_by_css_selector("[class='_2KpZ6l _173JMg _3AWRsL']").click()
driver.get("https://www.flipkart.com/")
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//div[text()='Deepak gahlot']")).perform()
driver.find_element_by_xpath("//div[text()='Orders']").click()
driver.find_element_by_xpath("//span[text()='Gritstones Striped Men Round Neck Multic...']").click()
driver.find_element_by_xpath("//span[text()='Cancel']").click()
dropdown = Select(driver.find_element_by_name("reasonList"))
dropdown.select_by_index(1)
time.sleep(3)
radiobutton2 = driver.find_elements_by_css_selector("[class='_1XFPmK']")
radiobutton2[1].click()
time.sleep(3)
driver.find_element_by_css_selector("[class='_2KpZ6l _2sblJX _3AWRsL']").click()



