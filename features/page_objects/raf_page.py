from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class RafPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "share_link_new_design": (By.XPATH, "//*[@class='raf-widget-code-header']/h5"),
        "share_link_old_design": (By.XPATH, "//*[@class='raf-widget-code']/h5"),


    }
