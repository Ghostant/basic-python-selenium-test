class SignIn():

    def __init__(self, driver):
        self.driver = driver

    def create_account(self):
        self.driver.find_element_by_xpath("//div[@id='ow250']").click()

    def create_account_for_you(self):
        self.driver.find_element_by_xpath('//*[@id="initialView"]/div[2]/div[3]/div/div/span[1]').click()
