from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com/')
name = input('Enter the name of the user or group:')
msg = input('Enter your message:')
count = int(input('Enter the no of times the message need to be send:'))
input('enter anythging after scaning qr code : ')
user = driver.find_element_by_xpath('//span[@title = "{}]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_3u328')
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
