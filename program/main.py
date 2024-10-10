import os
import time

from rich import print
from playwright.sync_api import sync_playwright

from login import retrieve_credentials, enter_credentials, wait_for_verification, goto_login
from attend import check_timeout, check_attendance, find_lectures

def attend_lectures(page):
    lecture_total = 0

    # First run always checks
    find_lectures(page, lecture_total)

    # Check every 30 minutes
    while True:
        check_timeout(page)
        lecture_total += check_attendance(page, lecture_total)

def microsoft_login(page):
    try:
        goto_login(page)
        username, password = retrieve_credentials()
        enter_credentials(page, username, password)
    except:
        print("[red]Incorrect username or password.[/red]")
        microsoft_login(page)

    wait_for_verification(page)

def initialize_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    return context

def main():
    os.system("cls")

    with sync_playwright() as playwright:
        context = initialize_browser(playwright)
        context.set_default_timeout(2000)
        page = context.new_page()

        try:
            microsoft_login(page)
            attend_lectures(page)
        except KeyboardInterrupt:
            os.system("cls")

if __name__ == "__main__":
    main()
