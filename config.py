# File: config.py
import os


class Config:
    TEST_URL = os.environ.get("TEST_URL", "https://web.tails-nonprod.com")
    FY_URL = os.environ.get("TEST_FY_URL", "https://frontyard.tails-nonprod.com")
    TEST_URL_SIGNIN = os.environ.get("TEST_URL", "https://web.tails-nonprod.com/gb/signin/")
    FY_HYPER_URL = os.environ.get("TEST_FY_URL", "http://frontyard.tails-nonprod.com")

    PROD_URL = os.environ.get("PROD_URL", "https://tails.com/gb/")
    PROD_URL_SIGNIN = os.environ.get("PROD_URL_SIGNIN", "https://tails.com/gb/signin")

    SELENIUM_REMOTE_URL = os.environ.get(
        "SELENIUM_REMOTE_URL", "http://selenium:4444/wd/hub"
    )
    WAIT_TIMEOUT = int(os.environ.get("WAIT_TIMEOUT", 50))
    FY_USERNAME = "qa_auto_tests"
    FY_PASSWORD = "itsasecret"

    @staticmethod
    def is_selenium_remote_url_set():
        return "SELENIUM_REMOTE_URL" in os.environ

    @staticmethod
    def get_os_env():
        return os.environ.get('OS_ENV')

    @staticmethod
    def should_execute_specific_code():
        return Config.get_os_env() == "http://selenium:4444"
