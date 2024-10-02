import os

from playwright.sync_api import sync_playwright

from login import retrieve_credentials, enter_credentials, wait_for_verification
from attend import check_timeout, check_attendance

def attend_lectures(page):
    lecture_total = 0
    first_run = True
    while True:
        check_timeout(page)
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
    os.system("cls")

    with sync_playwright() as playwright:
        context = initialize_browser(playwright)
        page = context.new_page()

        try:
            microsoft_login(page)
            attend_lectures(page)
        except KeyboardInterrupt:
            os.system("cls")

if __name__ == "__main__":
    main()
