from playwright.sync_api import sync_playwright

from login import microsoft_login
from attend import check_attendance

def attend_lectures(page):
    lecture_total = 0
    first_run = True
    while True:
        lecture_total += check_attendance(page, lecture_total, first_run)
        if first_run: first_run = False

def initialize_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    return context

def main():
    with sync_playwright() as playwright:
        context = initialize_browser(playwright)
        page = context.new_page()

        try:
            microsoft_login(page)
            attend_lectures(page)
        except KeyboardInterrupt:
            print("Exiting...")

if __name__ == "__main__":
    main()
