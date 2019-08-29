import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

userinput = input('What information are you looking for? ')
search_type = input('Do you want to do a strict search? Enter y or n: ')
if search_type == 'y':
    userinput = '"'+ userinput + '"'
    search_string = 'site:*.paloaltonetworks.com' + ' ' + userinput.lower()
else:
    search_string = 'site:*.paloaltonetworks.com' + ' ' + userinput.lower()

driver = webdriver.Chrome()
driver.get('https://google.com')
assert 'Google' in driver.title
search = driver.find_element_by_name('q')
search.clear()
search.send_keys(search_string)
search.send_keys(Keys.RETURN)
driver.quit()
