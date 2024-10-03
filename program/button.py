import time

def click_button(page, xpath):
    if page.locator("xpath=" + xpath).is_visible():
        page.click(xpath)
        time.sleep(0.5)
        return 1
    return 0
