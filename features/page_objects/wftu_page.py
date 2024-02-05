from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class WFTUPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {

        "wftu_get_started_continue": (By.XPATH, "//*[@class='btn btn-primary continue']"),
        "wftu_delivery_submit": (By.XPATH, "//button[@type='submit']"),
        "leave_as_it_is": (By.XPATH, "//*[@id='push-back-false']"),
        "push_back_month": (By.XPATH, "//*[@id='push-back-true']"),
        "confirm": (By.XPATH, "//button[contains(text(),'Confirm')]"),
        "next_full_order_date": (By.XPATH, "//span[@class='date']"),
        "wet_food_order_date": (By.XPATH, "//span[@class='date']/h2"),
        "view_my_deliveries": (By.XPATH, "//a[contains(@href,'/deliveries/')]"),
        "go_to_my_dashboard": (By.XPATH, "//*[@class='btn btn-secondary'][contains(text(),'Go to my dashboard')]"),
        "wftu_existing_order": (By.XPATH, "//*[@id='wftu-delivery-notification']/div/p")
    }
