import sys
import os
import datetime
import time
import shared

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from colorama import init
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


from config import Config

user = "shubhamr"
accessKey = "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"
lambda_test = 'https://@hub.lambdatest.com/wd/hub'
lambda_test_mobile_test = 'https://@mobile-hub.lambdatest.com/wd/hub'
print(user, accessKey)
print("printing user credentials")
print(user, accessKey)
print("printing done")


current_time = datetime.datetime.now()
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
selectors_hub_folder_path = "../selectors_hub/selectors_hub_ext.crx"
extension_path = os.path.join(current_path, selectors_hub_folder_path)


def before_all(context):
    print("Executing before all", file=sys.stderr)
    init()

    # Dir to output test artifacts
    context.artifacts_dir = 'artifacts'

    context.scenario_metadata_dict = {}
    context.feature_metadata = {'lighthouse': True}


def before_feature(context, feature):
    print("Before feature\n", file=sys.stderr)


def before_scenario(context, scenario):
    print("Before scenario\n", file=sys.stderr)
    print("User data:", context.config.userdata, file=sys.stderr)
    browser_name = context.config.userdata.get('browser')
    if context.config.userdata.get('browser') in (
            "headless", "chrome_lighthouse", "chrome_accessibility", "chrome",
            "iphone", "android", "hyper_iphone", "hyper_android"):

        driver = browser_config(context, browser_name, scenario)
        context.browser = driver
        # uc.Chrome = browser_config(context, browser_name, scenario)
        # context.browser = uc.Chrome

    elif "SELENIUM_REMOTE_URL" in os.environ:
        print("Before scenario and remote selenium\n", file=sys.stderr)
        print("OS env:", os.environ["SELENIUM_REMOTE_URL"], file=sys.stderr)
        Config.SELENIUM_REMOTE_URL = os.environ["SELENIUM_REMOTE_URL"]
        mobile_emulation = {"deviceName": "Pixel 2"}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation),
        options.add_argument("start-maximized")
        options.add_argument("enable-automation")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-infobars")
        if "lambdatest" not in os.environ["SELENIUM_REMOTE_URL"]:
            options.add_argument("--headless")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

        context.browser = webdriver.Remote(
            command_executor=os.environ["SELENIUM_REMOTE_URL"],
            options=options
        )

    elif "lighthouse" in scenario.effective_tags:
        context.port = 9222
        mobile_emulation = {"deviceName": "Pixel 2"}
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation),
        chrome_options.add_argument("disable-gpu"),
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--disable-storage-reset")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument('--remote-debugging-port=%s' % context.port)
        context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    else:
        mobile_emulation = {"deviceName": "Pixel 2"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation),
        chrome_options.add_argument("disable-popup-blocking")
        chrome_options.add_argument("disable-gpu"),
        chrome_options.add_argument("enable-automation")
        chrome_options.add_extension(extension_path)
        context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    shared.browser = context.config.userdata.get('browser')
    context.browser.set_page_load_timeout(70)


def after_scenario(context, scenario):
    print(f"after scenario: {scenario.status}", file=sys.stderr)
    if context.config.userdata.get('browser') in (
            "headless", "chrome_lighthouse", "chrome_accessibility", "chrome", "iphone", "android") or "lambdatest" in os.environ.get("SELENIUM_REMOTE_URL", ""):
        context.browser.execute_script(
            f"lambda-status={'passed' or 'completed' if scenario.status == 'passed' else 'failed'}")

    if scenario.status == 'failed' and context.config.userdata.get('browser') in ("chrome", "headless"):
        try:
            scenario_error_dir = os.path.join(context.artifacts_dir, 'feature_errors')
            make_dir(scenario_error_dir)
            scenario_file_path = os.path.join(scenario_error_dir, scenario.feature.name.replace(' ', '_')
                                              + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                              + '.png')
            context.browser.save_screenshot(scenario_file_path)
        except Exception:
            pass

    context.browser.delete_all_cookies()

    context.browser.quit()


def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)


def browser_config(context, browser_name, scenario, datestamp=current_time.strftime('%A %d-%m-%Y, %H:%M:%S')):
    if browser_name == "headless":
        mobile_emulation = {"deviceName": "Pixel 2"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation),
        options.add_argument("disable-popup-blocking"),
        options.add_argument("disable-gpu"),
        options.add_argument("--headless")
        options.add_argument("enable-automation")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-infobars")
        from webdriver_manager.chrome import ChromeDriverManager
        browser = webdriver.Chrome()
        return browser

    if browser_name == "iphone":
        safari_options = SafariOptions()

        lt_options_iphone = {
            "user": user,
            "accessKey": accessKey,
            "build": "iphone :" + f"{datestamp}",
            "project": "tails_iphone",
            "name": f"{scenario}",
            "platformName": "ios",
            "platformVersion": "16",
            "deviceName": "iPhone 14 Pro",
            "w3c": True,
            "idleTimeout": "300",
            "tunnel": True,
            "console": True,
            "network": False,
            "visual": True,
            "terminal": True,
            "isRealMobile": True,
            "dynamicAllocation": True,
            "smartWait": 40,
            'goog:chromeOptions': {
                'args': ['extensionLoadTimeout=60000', '–disable-notifications', 'enable-automation', 'disable-gpu',
                         '--disable-gpu',
                         'page_load_strategy=eager']}

        }

        safari_options.set_capability('LT:Options', lt_options_iphone)
        safari_options.set_capability('platformName', "iOS")
        browser_lambda_iphone = webdriver.Remote(
            command_executor=lambda_test_mobile_test,
            options=safari_options)
        print("printing lt options")
        print(lt_options_iphone)
        print(safari_options)
        print("printing lt options completed")
        return browser_lambda_iphone

    if browser_name == "android":
        chrome_options = ChromeOptions()

        lt_options_android = {
            "user": user,
            "accessKey": accessKey,
            "build": "lambda_Android :"f"{datestamp}",
            "name": f"{scenario}",
            "platformName": "android",
            "browserVersion": "latest",
            "deviceName": "Galaxy S21 5G",
            "platformVersion": "13",
            "browserName": "Chrome",
            "project": "tails_test",
            "visual": True,
            "network": False,
            "video": True,
            "console": True,
            "idleTimeout": "300",
            "tunnel": True,
            "isRealMobile": True,
            "terminal": True,
            "w3c": True,
            "dynamicAllocation": True,
            "smartWait": 40
        }

        chrome_options.set_capability('LT:Options', lt_options_android)
        browser_lambda_android = webdriver.Remote(
            command_executor=lambda_test_mobile_test,
            options=chrome_options)
        return browser_lambda_android

    if browser_name == "chrome":
        chrome_options = ChromeOptions()

        lt_options_chrome = {
            "user": user,
            "accessKey": accessKey,
            "build": "chrome :"f"{datestamp}",
            "project": "tails_test",
            "name": f"{scenario}",
            "platformName": "Windows 10",
            "idleTimeout": "300",
            "tunnel": True,
            "console": True,
            "network": False,
            "visual": True,
            "dynamicAllocation": "true",
            'goog:chromeOptions': {
                'args': ['extensionLoadTimeout=60000', '–disable-notifications', 'enable-automation', 'disable-gpu',
                         '--disable-gpu',
                         '--window-size=411,731', 'page_load_strategy=eager']},
            "smartWait": 60

        }

        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("disable-gpu"),
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--disable-infobars")

        chrome_options.set_capability('LT:Options', lt_options_chrome)
        browser_lambda_chrome = webdriver.Remote(
            command_executor=lambda_test,
            options=chrome_options)

        return browser_lambda_chrome

    if browser_name == "chrome_lighthouse":
        chrome_options = ChromeOptions()

        lt_options_chrome_lighthouse = {
            "user": user,
            "accessKey": accessKey,
            "build": "chrome :"f"{datestamp}",
            "project": "tails_test",
            "name": f"{scenario}",
            "platformName": "Windows 10",
            "idleTimeout": "300",
            "tunnel": True,
            "console": True,
            "network": False,
            "visual": True,
            "dynamicAllocation": "true",
            'goog:chromeOptions': {
                'args': ['–disable-notifications', 'enable-automation', 'disable-gpu', '--headless', '--clear-storage'
                                                                                                     '--disable-gpu',
                         '--window-size=411,731',
                         '--no-sandbox', '--remote-debugging-port=9222', 'extensionLoadTimeout=60000',
                         'page_load_strategy=eager']},
            "smartWait": 40
        }

        chrome_options.set_capability('LT:Options', lt_options_chrome_lighthouse)
        browser_lambda_chrome_lighthouse = webdriver.Remote(
            command_executor=lambda_test,
            options=chrome_options)

        return browser_lambda_chrome_lighthouse

    if browser_name == "chrome_accessibility":
        chrome_options = ChromeOptions()

        lt_options_chrome_accessibility = {
            "user": user,
            "accessKey": accessKey,
            "build": "chrome :"f"{datestamp}",
            "project": "tails_test",
            "name": f"{scenario}",
            "platformName": "Windows 10",
            "idleTimeout": "300",
            "tunnel": True,
            "console": True,
            "network": False,
            "visual": True,
            "dynamicAllocation": "true",
            'goog:chromeOptions': {'args': ['enable-automation', 'disable-gpu', '--headless',
                                            '--disable-gpu', '--no-sandbox', 'extensionLoadTimeout=60000',
                                            'page_load_strategy=eager']},

            "smartWait": 40
        }

        chrome_options.set_capability('LT:Options', lt_options_chrome_accessibility)
        browser_lambda_chrome_accessibility = webdriver.Remote(
            command_executor=lambda_test,
            options=chrome_options)

        return browser_lambda_chrome_accessibility

