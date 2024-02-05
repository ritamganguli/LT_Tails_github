from behave import when, then, use_step_matcher
import time

from features.page_objects.raf_page import RafPage
from features.page_objects.dashboard_page import DashboardPage

use_step_matcher("re")


@when("Select RAF page")
def _(context):
    dashboard_page = DashboardPage(context)
    time.sleep(15)
    dashboard_page.hamburger_menu.click()
    time.sleep(10)
    dashboard_page.raf_page_select.click()
    time.sleep(5)


@then('Confirm "(.*)" in store "(.*)" displays')
def _(context, raf, store):
    raf_page = RafPage(context)
    # The following code is segmented into locales because the RAf pages have different header tags (???) for
    # different locales. elements are split into new and old designs
    if store == "GB":
        header = raf_page.share_link_new_design
        assert raf in header.text
    if store == "FR":
        header_fr = raf_page.share_link_old_design
        assert raf in header_fr.text
    if store == "DE":
        header_de = raf_page.share_link_old_design
        assert raf in header_de.text
