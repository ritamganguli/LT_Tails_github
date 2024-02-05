from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException,
)

from .base_page_object import BasePage


class NavigationPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def close_browser(self):
        self.browser.close()

    def login_button(self):
        element = self.find_xpath("//*[@data-cy='loginButton']")
        self.browser.execute_script('arguments[0].click();', element)

    def is_dashboard_ftw_loaded(self, ftw, timeout=15):
        wait = WebDriverWait(self.browser, timeout)
        try:
            # Try to wait for the primary element to become present and then return it
            return wait.until(EC.presence_of_element_located((By.XPATH, f"//*[@class='container']//*[contains(text(), '{ftw}')]")))
        except TimeoutException:
            # If waiting for the primary element fails, try to wait for the secondary element
            try:
                return wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[@class='dog-image']")))
            except TimeoutException:
                # If neither element is found within the timeout, print an error message and return None
                print("Neither the flea tick and worm page or the dog image page was found within the timeout.")
                return None

    def is_dashboard_delivery_loaded(self, delivery, timeout=15):
        wait = WebDriverWait(self.browser, timeout)
        try:
            # Try to wait for the primary element to become present and then return it
            return wait.until(EC.presence_of_element_located((By.XPATH, f"//div[2]/h1[contains(text(), '{delivery}')]")))
        except TimeoutException:
            # If waiting for the primary element fails, try to wait for the secondary element
            try:
                return wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[@class='dog-image']")))
            except TimeoutException:
                # If neither element is found within the timeout, print an error message and return None
                print("Neither the delivery page or the dog image page was found within the timeout.")
                return None

    def is_dashboard_raf_loaded(self, raf, timeout=15):
        wait = WebDriverWait(self.browser, timeout)
        try:
            # Try to wait for the primary element to become present and then return it
            return wait.until(EC.presence_of_element_located
                              ((By.XPATH, f"//*[@class='credit_info claim']/h3[contains(text(), '{raf}')]")))
        except TimeoutException:
            # If waiting for the primary element fails, try to wait for the secondary element
            try:
                return wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[@class='dog-image']")))
            except TimeoutException:
                # If neither element is found within the timeout, print an error message and return None
                print("Neither the refer a friend page or the dog image page was found within the timeout.")
                return None

    def is_dashboard_account_loaded(self, account, timeout=15):
        wait = WebDriverWait(self.browser, timeout)
        try:
            # Try to wait for the primary element to become present and then return it
            return wait.until(
                EC.presence_of_element_located((By.XPATH, f"//*[@class='content']//*[contains(text(), '{account}')]")))
        except TimeoutException:
            # If waiting for the primary element fails, try to wait for the secondary element
            try:
                return wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[@class='dog-image']")))
            except TimeoutException:
                # If neither element is found within the timeout, print an error message and return None
                print("Neither the account page or the dog image page was found within the timeout.")
                return None

    def is_dashboard_profile_loaded(self, name, timeout=15):
        wait = WebDriverWait(self.browser, timeout)
        try:
            # Try to wait for the primary element to become present and then return it
            return wait.until(EC.presence_of_element_located((By.XPATH, f"//*/h1/span[contains(text(), '{name}')]")))
        except TimeoutException:
            # If waiting for the primary element fails, try to wait for the secondary element
            try:
                return wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[@class='dog-image']")))
            except TimeoutException:
                # If neither element is found within the timeout, print an error message and return None
                print("Neither the profile page or the dog image page was found within the timeout.")
                return None

    def is_dashboard_feeding_plan_loaded(self, update, timeout=15):
        wait = WebDriverWait(self.browser, timeout)
        try:
            # Try to wait for the primary element to become present and then return it
            return wait.until(
                EC.presence_of_element_located((By.XPATH, f"//*[@class='top-block']//*[contains(text(), '{update}')]")))
        except TimeoutException:
            # If waiting for the primary element fails, try to wait for the secondary element
            try:
                return wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[@class='dog-image']")))
            except TimeoutException:
                # If neither element is found within the timeout, print an error message and return None
                print("Neither the feeding plan page or the dog image page was found within the timeout.")
                return None

    def is_shop_loaded(self, recommend, timeout=20):
        wait = WebDriverWait(self.browser, timeout)
        try:
            # Try to wait for the primary element to become present and then return it
            return wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//*[@data-testid='plp-recommended-product']/h4[contains(text(), '{recommend}')]")))
        except TimeoutException:
            # If waiting for the primary element fails, try to wait for the secondary element
            try:
                return wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[@class='dog-image']")))
            except TimeoutException:
                # If neither element is found within the timeout, print an error message and return None
                print("Neither the shop page or the dog image page was found within the timeout.")
                return None

    def escape_keyboard(self):
        try:
            # Try to find the 'body' element and send the ESCAPE key
            body_element = self.browser.find_element(By.TAG_NAME, "body")
            body_element.send_keys(Keys.ESCAPE)
        except NoSuchElementException:
            # If the 'body' element is not found, just pass
            pass

    def dismiss_keyboard(self):
        # Now execute the JavaScript to blur the active element
        self.browser.execute_script("document.activeElement.blur();")

    def check_height_page_go_bottom_page(self):
        # Step 1: Get the vertical height of the page
        height = self.browser.execute_script("return document.body.scrollHeight")

        # Step 2: Check if the page is at the top or in the middle
        current_position = self.browser.execute_script("return window.pageYOffset")
        if current_position < height / 2:
            # Step 3: Scroll to the bottom of the page
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            print("At the bottom of the page")

    def check_height_page_go_middle_of_page(self):
        # Step 1: Get the vertical height of the page
        height = self.browser.execute_script("return document.body.scrollHeight")

        # Step 2: Scroll to the middle of the page
        middle_height = height / 2
        self.browser.execute_script(f"window.scrollTo(0, {middle_height})")

        # Optional: You might want to check if the scroll was successful
        current_position = self.browser.execute_script("return window.pageYOffset")
        if current_position >= middle_height:
            print("At the middle of the page")
        else:
            print("Scrolling to the middle of the page was not successful")

    def check_height_page_go_top_of_page(self):
        # Step 1: Get the vertical height of the page
        height = self.browser.execute_script("return document.body.scrollHeight")

        # Step 2: Calculate the height of the top half of the page
        top_half_height = height / 2

        # Step 3: Scroll to the top half of the page
        self.browser.execute_script(f"window.scrollTo(0, {top_half_height})")

        # Optional: Check if the scroll was successful
        current_position = self.browser.execute_script("return window.pageYOffset")
        if current_position > top_half_height:
            print("Scrolled to the top half of the page")
        else:
            print("Scrolling to the top half of the page was not successful")

    locator_dictionary = {
        "continue_sign": (By.XPATH, '//*[@id="hero-text"]/div/a[2]'),
        "log_in": (By.LINK_TEXT, "Log in"),
        "log_out": (By.LINK_TEXT, "Log Out"),
        "home_logo": (By.XPATH, "(//div[@class='logo'])"),
        "discovery": (By.CSS_SELECTOR, "#discovery-body"),
        "signup": (By.XPATH, '//*[@id="hero-text"]/div/a[2]'),
        "pet_form": (By.CSS_SELECTOR, "#form_pets"),
        "home_menu": (By.CSS_SELECTOR, "label[for=hamburger]"),
        "menu_log_out": (
            By.XPATH,
            '//*[@id="other-links-side"]/div/a[2]/div[contains(text(),"Log Out")]',
        ),
        "de_menu_log_out": (
            By.XPATH,
            '//*[@id="other-links-side"]/div/a[2]/div[contains(text(),"Abmelden")]',
        ),
        "nl_menu_log_out": (By.XPATH, '//*[@id="other-links-side"]/div/a[2]/div[contains(text(), "Uitloggen")]'),
        "fr_menu_log_out": (By.XPATH, '//*[@id="other-links-side"]/div/a[2]/div'),
        "account_login": (By.CSS_SELECTOR, '#tails-view-2 > div > div > button'),
        "menu_log_in": (By.XPATH, '//*[@id="other-links-side"]/div/a[1]/div[2]'),
        "_pets_another_dog": (By.CSS_SELECTOR, "#add_pet"),
        "pets_another_dog": (By.ID, "add_pet"),
        "two_dogs_profile": (
            By.XPATH,
            "//*[@id='form_pets']/div[1]/div[3]/div[1]/div[1]/h5/span",
        ),
        "three_dogs_profile": (
            By.XPATH,
            "//*[@id='form_pets']/div[1]/div[5]/div[1]/div[1]/h5/span",
        ),
        "another_dog_link": (By.XPATH, "//*[@id='form_pets']/div[1]/div[1]/p/a[contains(text(),'View Feeding Plan')]"),
        "forgot_password": (By.LINK_TEXT, "Forgotten password?"),

    }
