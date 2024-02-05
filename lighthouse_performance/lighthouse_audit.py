import datetime
import json
import os
import time
import subprocess
import csv

from datetime import datetime
from features.page_objects.base_page_object import BasePage
from lighthouse_performance.lighthouse_report import LightHelper

class LighthouseAudit(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def run_audit(self):
        helper = LightHelper(self)
        url = self.browser.current_url

        url_ = f"{helper.set_filename(url)}"
        print(url_)

        name = "light_report"
        getdate = datetime.now().strftime("%m-%d-%y")
        time_ = datetime.now().strftime("%H:%M:%S")
        date_time = getdate + '_' + time_

        # Set the Lighthouse options
        mobile_preset = 'perf'
        chrome_flags = '--chrome-flags="--no-sandbox --headless --disable-gpu"'
        disable_storage_reset = '--disable-storage-reset="true"'
        port = '--port=9222'
        max_wait = '--max-wait-for-load=30000'

        relative_path = os.path.abspath(os.path.dirname(__file__))

        json_filename = os.path.join(relative_path, name + '_' + getdate + '.report.json')

        # prints parent window title
        print("Parent window title: " + self.browser.title)

        # get current window handle
        parent_window = self.browser.current_window_handle

        # get first child window
        child_window = self.browser.window_handles

        for w in child_window:
            # switch focus to child window
            if (w != parent_window):
                self.browser.switch_to.window(w)
            break
        time.sleep(0.9)
        print("Child window title: " + self.browser.title)

        subprocess.run(
            f'lighthouse {url} {port} {chrome_flags} {disable_storage_reset} --preset={mobile_preset} '
            f'{max_wait} --output=json --output-path=' + json_filename,
            shell=True)

        time.sleep(10)

        # open the json file and start processing it
        with open(json_filename, encoding="utf8") as json_data:
            loaded_json = json.load(json_data)
        print(loaded_json)

        # Extract performance metrics
        first_contentful_paint = loaded_json["audits"]["first-contentful-paint"]["displayValue"]
        speed_index = loaded_json["audits"]["speed-index"]["displayValue"]
        largest_contentful_paint = loaded_json["audits"]["largest-contentful-paint"]["displayValue"]
        performance = loaded_json["categories"]["performance"]["score"]

        # Save metrics to results.csv
        csv_output_file = os.path.join(relative_path, 'results.csv')

        # Check if the CSV file exists
        file_exists = os.path.isfile(csv_output_file)

        # Write the CSV file with headers if it does not exist or append new rows if it exists
        with open(csv_output_file, 'a', newline='') as csv_file:
            fieldnames = ['url_id', 'url', 'FCP', 'SI', 'LCP', 'Perf', 'date_time']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write headers if the file does not exist
            if not file_exists:
                writer.writeheader()

            # Write a new row with the metrics
            writer.writerow({
                'url_id': url,
                'url': url_,
                'FCP': first_contentful_paint,
                'SI': speed_index,
                'LCP': largest_contentful_paint,
                'Perf': performance,
                'date_time': date_time

            })

        print("Lighthouse metrics saved to:", csv_output_file)

        # Remove the JSON file
        os.remove(json_filename)
        print("JSON file removed:", json_filename)

        print("Audit Done")

        time.sleep(5)
        self.browser.switch_to.window(parent_window)
        self.browser.get(url)

