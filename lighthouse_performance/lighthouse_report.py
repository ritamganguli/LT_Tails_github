import os
import time
from features.page_objects.base_page_object import BasePage
from lighthouse_performance.light_helper import LightHelper
import subprocess


class LighthouseReport(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def run_report(self):
        helper = LightHelper(self)
        url = self.browser.current_url

        # Set the Lighthouse options

        mobile_preset = 'perf'
        chrome_flags = '--chrome-flags="--headless"'
        disable_storage_reset = '--disable-storage-reset="true"'
        port = '--port=9222'
        max_wait = '--max-wait-for-load=30000'

        relative_path = os.path.abspath(os.path.dirname(__file__))

        report_file = os.path.join(relative_path, '_' + helper.set_filename(url) + '.html')

        self.browser.get('about:blank')
        print(report_file)

        subprocess.run(
            f"lighthouse {url} {port} {chrome_flags} {disable_storage_reset} --preset={mobile_preset} "
            f"{max_wait} --output=html --output-path={report_file}",
            shell=True)
        time.sleep(30)

        print("Report Done")

        time.sleep(5)
        self.browser.get('about:blank')
        self.browser.get(url)
