import os
import time
from dotenv import load_dotenv
from .base.driver_base import DriverBase

load_dotenv()

## Creds
username = os.getenv('USERNAME') 
password = os.getenv('PASSWORD') 

class Meta():
    def __init__(self) -> None:
        self.base = DriverBase(what="meta")
        self.driver = self.base.driver()
        self.meta_url = "https://facebook.com/login/"
        
        ## init
        self.login()
        # all otehr things between here
        self.logout()
        
        ## Close
        self.driver.close()

    def login(self):
        self.base.goto(driver=self.driver, url=self.meta_url)    
        self.base.find_element(driver=self.driver, selector_type="name", element="email").send_keys(username)
        time.sleep(1)
        self.base.find_element(driver=self.driver, selector_type="name", element="pass").send_keys(password)
        time.sleep(1)
        self.base.find_element(driver=self.driver, selector_type="name", element="login").click()
        time.sleep(5)

    def logout(self):
        self.base.find_element(driver=self.driver, selector_type="css_selector", element="div[aria-label='Your profile']").click()
        time.sleep(5)
        self.base.find_element(driver=self.driver, selector_type="xpath", element="//*[text()='Log out']").click()
