from selenium import webdriver

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get("https://www.wikipedia.org/")

search_field = driver.find_element_by_id("searchInput")
search_field.send_keys("Test automation")

search_button = driver.find_element_by_xpath("//*[@id='search-form']/fieldset/button")
search_button.click()

assert "Test automation" in driver.title

driver.quit()