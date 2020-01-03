from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

time.sleep(25)

names = ["Baitalika"]

for name in names:
    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    person.click()
    for i in range(1, 3):
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
    msg_got = driver.find_elements_by_css_selector(
'span._F7Vk selectable-text.invisible-space.copyable-text')
    msg = [message.text for message in msg_got]

    print(msg[1])
