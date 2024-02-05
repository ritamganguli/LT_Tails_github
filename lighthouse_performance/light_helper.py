import re
from features.page_objects.base_page_object import BasePage


class LightHelper(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    @staticmethod
    def set_filename(url):
        # Find positions of ".com" and last "/"
        start_pos = url.find('.com') + 4
        end_pos = url.rfind('/')

        # Extract the substring between these positions and replace "/" with "_"
        substring = url[start_pos:end_pos].replace('/', '_')

        # Remove the first "_"
        substring = substring.replace('_', '', 1)

        # Remove integers from the substring
        substring_url = re.sub(r'\d+', '', substring)

        print(substring_url)

        return substring_url
