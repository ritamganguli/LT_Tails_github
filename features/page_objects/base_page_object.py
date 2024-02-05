import sys
import time
import traceback
from config import Config
from contextlib import contextmanager

from furl import furl
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException, WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
_WAIT_TIMEOUT = Config.WAIT_TIMEOUT


class BasePage(object):

    def __init__(self, browser,
                 base_url=Config.TEST_URL,
                 test_url_sign=Config.TEST_URL_SIGNIN,
                 fy_url=Config.FY_URL,
                 fy_hyper_url=Config.FY_HYPER_URL,
                 prod_url=Config.PROD_URL,
                 prod_url_sign=Config.PROD_URL_SIGNIN):
        self.base_url = base_url
        self.test_url_sign = test_url_sign
        self.fy_url = fy_url
        self.fy_hyper_url = fy_hyper_url
        self.prod_url = prod_url
        self.prod_url_sign = prod_url_sign
        self.browser = browser
        self.timeout = Config.WAIT_TIMEOUT


    def set_test_url_params(self, params):
        self.base_url = furl(self.base_url).set(params).url

    def full_path(self, relative_path):
        return furl(self.base_url).add(path=relative_path).url

    def goto(self, relative_path):
        self.browser.get(self.full_path(relative_path))

    def goto_fy(self):
        self.browser.get(self.fy_url)

    def goto_prod(self):
        self.browser.get(self.prod_url)

    def goto_prod_signin(self):
        self.browser.get(self.prod_url_sign)

    def visit(self, url):
        self.browser.get(url)

    @contextmanager
    def iframe(self, css_selector):
        _iframe = self.wait_for(css_selector, EC.frame_to_be_available_and_switch_to_it)
        yield _iframe
        self.browser.switch_to.default_content()

    def input_text(self, css_selector, text, typing_delay=None):
        _input = self.wait_for(css_selector, EC.element_to_be_clickable)

        if not typing_delay:
            _input.send_keys(text)
        else:
            for letter in text:
                _input.send_keys(letter)
                time.sleep(typing_delay)

        return _input

    def click_element_(self, css_selector, _wait=_WAIT_TIMEOUT):
        element = self.wait_for(css_selector, EC.element_to_be_clickable, _wait=_wait)
        element.click()
        return element

    def click_element_xpath(self, xpath, _wait=_WAIT_TIMEOUT):
        element = self.wait_for(xpath, EC.element_to_be_clickable, _wait=_wait)
        element.click()
        return element

    def wait_for(self, css_selector, ec, _wait=_WAIT_TIMEOUT):
        time.sleep(7)
        wait = WebDriverWait(self.browser, _wait)
        element = wait.until(ec((By.CSS_SELECTOR, css_selector)))
        return element

    def select_by_input_value(self, css_selector):
        """Get the value attribute of an input field"""
        input_element = WebDriverWait(self.browser, 70).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        _get_text = input_element.get_attribute("value")
        return _get_text

    def select_by_text(self, css_selector, text):
        """Selects option by visible text in dropdown list"""
        option_selector = WebDriverWait(self.browser, 70).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        option_selector = Select(option_selector)
        option_selector.select_by_visible_text(text)
        return option_selector

    def find_element(self, by, value):
        wait = WebDriverWait(self.browser, 70)
        return wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, xpath):
        wait = WebDriverWait(self.browser, 70)
        return wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_elements_by_locator(self, by, selector_type):
        wait = WebDriverWait(self.browser, 70)
        return wait.until(EC.presence_of_all_elements_located((by, selector_type)))

    def assert_not_visible(self, css_selector, _wait=_WAIT_TIMEOUT):
        try:
            return self.wait_for(css_selector, EC.element_to_be_clickable, _wait=_wait)
        except NoSuchElementException:
            return True

    def scroll_to_bottom_of_page(self):
        html = self.browser.find_element(By.TAG_NAME, "html")
        html.send_keys(Keys.END)

    def scroll_down_page(self):
        html = self.browser.find_element(By.TAG_NAME, "html")
        html.send_keys(Keys.PAGE_DOWN)

    def find(self, element):
        wait = WebDriverWait(self.browser, 40)
        return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))

    def find_xpath_not_dictionary(self, element):
        wait = WebDriverWait(self.browser, 40)
        return wait.until(EC.presence_of_element_located((By.XPATH, element)))

    def find_xpath(self, element):
        wait = WebDriverWait(self.browser, 40)
        return wait.until(EC.presence_of_element_located((By.XPATH, element)))

    def assert_element_is_not_visible(self, xpath):
        wait = WebDriverWait(self.browser, 40)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            raise Exception("Element should not be visible")
        except NoSuchElementException:
            pass

    def assert_element_not_visible(self, xpath):
        # from selenium.common.exceptions import TimeoutException
        try:
            if self.browser.find_elements(By.XPATH, xpath):
                raise Exception('element should not be visible')
        except TimeoutException:
            pass

    def number_of_windows(self, num_windows, _wait=_WAIT_TIMEOUT):
        return WebDriverWait(self.browser, _wait).until(EC.number_of_windows_to_be(num_windows))

    def wait_for_element_to_be_invisible(self, selector, _wait=_WAIT_TIMEOUT):
        WebDriverWait(self.context, _wait).until(EC.invisibility_of_element_located(selector))

    def scroll_up_page(self):
        html = self.browser.find_element(By.TAG_NAME, "html")
        html.send_keys(Keys.PAGE_UP)

    def get_select_element(self, element):
        """useful to access elements with options like select dropdowns"""
        element = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.ID, element)))
        return Select(element)

    def click_element_js(self, element):
        """useful to access elements with options like select dropdowns"""
        self.browser.execute_script("arguments[0].click();", element)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except (TimeoutException, NoSuchElementException):
                    traceback.print_exc()

                    # Additional code to handle NoSuchElementException
                    if isinstance(self.browser, BasePage):
                        print("Element not found. Analyzing page source.")
                        page_source = self.browser.page_source
                        keywords = ["something went wrong", "Oops", "504", "503", "experiencing a rush of new dogs",
                                    "Dalmatians", "Uh - Oh!"]
                        found_keywords = [word for word in keywords if word in page_source]
                        if found_keywords:
                            print("Found the following words/phrases in the page source:", found_keywords)
                            print("Current URL:", self.browser.current_url)
                        else:
                            print("None of the specified keywords were found in the page source.")

                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                    print("Success Element target found:" + what)
                except (TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        EC.element_to_be_clickable(self.locator_dictionary[what])
                    )
                except (TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    # Try to locate the element with text 'Oops'
                    try:
                        element = self.browser.find_element(By.XPATH, "//h1[normalize-space()='Oops']")
                    except NoSuchElementException:
                        # If not found, try to locate the element with text 'OEPS!'
                        element = self.browser.find_element(By.XPATH, "//h1[normalize-space()='OEPS!']")

                    # Check if either element is found
                    if element:
                        current_url = self.browser.current_url
                        print("Element found at URL:", current_url)
                        assert False, "Test failed: Element with 'Oops' or 'OEPS!' found on the page."
                except NoSuchElementException:
                    print("Element with 'Oops' or 'OEPS!' not found")

                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)
            return False

    @staticmethod
    def method_missing():
        print("method missing", file=sys.stderr)
