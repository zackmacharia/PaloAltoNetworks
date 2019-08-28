import webbrowser
from selenium import webdriver
# For this script to work you'll need to install
# Chromedriver and put it in path or if you are
# using virtualenv place it under env/bin/. env being
# your virutal environment folder
driver = webdriver.Chrome()
driver.get('https://google.com')

search_input_box = driver.find_element_by_name('q')
search_input_box.send_keys('test search')
