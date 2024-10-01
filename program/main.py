from playwright.sync_api import sync_playwright

from login import wait_for_verification, enter_credentials, retrieve_credentials
from attend import check_attendance

def attend_lectures(page):
    lecture_total = 0
    first_run = True
    while True:
        lecture_total += check_attendance(page, lecture_total, first_run)
        if first_run: first_run = False

def microsoft_login(page):
    username, password = retrieve_credentials()
    enter_credentials(page, username, password)
    wait_for_verification(page)

def initialize_browser(playwright):
    browser = playwright.chromium.launch(headless=True)
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
