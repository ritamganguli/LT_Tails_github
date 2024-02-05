import csv
import time
from datetime import datetime
from axe_selenium_python import Axe
import os
from .base_page_object import BasePage


class AccessibilityPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    @staticmethod
    def perform_accessibility_audit_first_page(context):
        # Write results to a CSV file
        name = "accessibility_results.csv"
        folder_name = "accessibility_reports"

        # Get the current working directory (where your script is located)
        script_directory = os.path.dirname(os.path.realpath(__file__))

        # Navigate two levels up to get the project directory
        project_directory = os.path.abspath(os.path.join(script_directory, os.pardir, os.pardir))

        # Combine the project directory with the desired output folder name
        output_folder = os.path.join(project_directory, folder_name)

        # Check if the folder exists, and create it if it doesn't
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Combine the output folder with the desired output file name
        output_file = os.path.join(output_folder, name)

        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Flag to track if header has been written
        header_written = False

        # Open the file in write mode and create a CSV writer
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Perform accessibility scan using Axe-Core
            axe = Axe(context.browser)
            axe.inject()
            results = axe.run()
            time.sleep(7)

            # Write the accessibility results to the CSV file
            for result in results['violations']:
                violation = result['id']
                description = result['description']
                help_text = result['help']
                help_url = result['helpUrl']
                impact = result['impact']

                # Check if the header has been written
                if not header_written:
                    # Write the header row
                    writer.writerow(
                        ['current_time', 'Violation', 'Description', 'Help', 'HelpUrl', 'Impact', 'Test URL'])

                    header_written = True

                # Write the row to the CSV file
                writer.writerow(
                    [current_time, violation, description, help_text, help_url, impact, context.browser.current_url])

                time.sleep(7)

    def perform_accessibility_audit_other_page(self, context):
        # Write results to a CSV file
        name = "accessibility_results.csv"
        folder_name = "accessibility_reports"

        # Get the current working directory (where your script is located)
        script_directory = os.path.dirname(os.path.realpath(__file__))

        # Navigate two levels up to get the project directory
        project_directory = os.path.abspath(os.path.join(script_directory, os.pardir, os.pardir))

        # Combine the project directory with the desired output folder name
        output_folder = os.path.join(project_directory, folder_name)

        # Check if the folder exists, and create it if it doesn't
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Combine the output folder with the desired output file name
        output_file = os.path.join(output_folder, name)

        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Flag to track if header has been written
        header_written = True

        # Open the file in write mode and create a CSV writer
        with open(output_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            time.sleep(3)

            # Perform accessibility scan using Axe-Core
            axe = Axe(context.browser)
            axe.inject()
            results = axe.run()
            time.sleep(7)

            # Write the accessibility results to the CSV file
            for result in results['violations']:
                violation = result['id']
                description = result['description']
                help_text = result['help']
                help_url = result['helpUrl']
                impact = result['impact']

                # Check if the header has been written
                if not header_written:
                    # Write the header row
                    writer.writerow(
                        ['current_time', 'Violation', 'Description', 'Help', 'HelpUrl', 'Impact', 'Test URL'])

                    header_written = True

                # Write the row to the CSV file
                writer.writerow(
                    [current_time, violation, description, help_text, help_url, impact, context.browser.current_url])

                time.sleep(7)
