import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

class DriverBase():
    def __init__(self, what: str = None) -> None:
        self.what = what

    def driver(self) -> Chrome:
        chrome_options = self.chrome_options()
        driver = Chrome(options=chrome_options)
        driver.maximize_window()
        return driver

    def goto(self, driver: Chrome, url: str) -> None:
        driver.get(url)
        time.sleep

    def chrome_options(self) -> ChromeOptions:
        chrome_options = ChromeOptions()
        if self.what in ['meta']:
            # turn off popup notifications for meta, update if you want for more
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.page_load_strategy = 'eager'
        return chrome_options

    def find_element(self, driver: Chrome, selector_type: str, element: str):
        if selector_type == "id":
            return driver.find_element(By.ID, element)
        elif selector_type == "name":
            return driver.find_element(By.NAME, element)
        elif selector_type == "xpath":
            return driver.find_element(By.XPATH, element)
        elif selector_type == "link_text":
            return driver.find_element(By.LINK_TEXT, element)
        elif selector_type == "partial_link_text":
            return driver.find_element(By.PARTIAL_LINK_TEXT, element)
        elif selector_type == "tag_name":
            return driver.find_element(By.TAG_NAME, element)
        elif selector_type == "class_name":
            return driver.find_element(By.CLASS_NAME, element)
        elif selector_type == "css_selector":
            return driver.find_element(By.CSS_SELECTOR, element)
        else:
            raise ValueError(f"Unknown selector type: {selector_type}")

    def scroll_to_bottom(self, driver: Chrome) -> BeautifulSoup:
        ## Scrolls to the bottom of the page and returns an beacutifull soup obj
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        return soup
