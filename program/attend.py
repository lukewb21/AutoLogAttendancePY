import os
import time
from datetime import datetime

def click_buttons(page):
    clicked = 0
    if page.locator("xpath=//*[@id=\"pbid-buttonFoundHappeningNowButtonsOneHere\"]").is_visible():
        page.click("xpath=//*[@id=\"pbid-buttonFoundHappeningNowButtonsOneHere\"]")
        clicked += 1
    if page.locator("xpath=//*[@id=\"pbid-buttonFoundHappeningNowButtonsTwoHere\"]").is_visible():
        page.click("xpath=//*[@id=\"pbid-buttonFoundHappeningNowButtonsTwoHere\"]")
        clicked += 1
    return clicked

def get_current_minute(page):
    current_datetime = datetime.strptime(page.locator("xpath=//*[@id=\"jsTime\"]").inner_text(), "%d/%m/%Y %H:%M:%S")
    return current_datetime.strftime("%M")

def check_attendance(page, lecture_total, first_run):
    attend_target_minutes = {"01", "31"}
    refresh_target_minutes = {"59", "44", "29", "14"}
    current_minute = get_current_minute(page)

    clicked = 0
    if current_minute in attend_target_minutes or first_run:
        clicked += click_buttons(page)
        os.system("cls")
        print("Signed in as " + page.locator("xpath=//*[@id=\"username\"]/span").inner_text())
        print("Lectures attended today: " + str(lecture_total + clicked))
        time.sleep(60)
    elif current_minute in refresh_target_minutes:
        page.reload()
        time.sleep(60)
    time.sleep(1)

    return clicked
