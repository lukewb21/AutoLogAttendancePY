import os
import time

def wait_for_verification(page):
    time.sleep(2)
    print("Please verify your login with the following code: " + page.locator("xpath=//*[@id=\"idRichContext_DisplaySign\"]").inner_text())
    while True:
        if page.locator("//*[@id=\"idA_SAASTO_Resend\"]").is_visible():
            time.sleep(10)
            page.click("xpath=//*[@id=\"idA_SAASTO_Resend\"]")
            os.system("cls")
            print("Please verify your login with the following code: " + page.locator("xpath=//*[@id=\"idRichContext_DisplaySign\"]").inner_text())
        elif page.locator("xpath=//*[@id=\"idBtn_Back\"]").is_visible():
            page.click("xpath=//*[@id=\"idBtn_Back\"]")
            break
        time.sleep(1)
    os.system("cls")
    time.sleep(2)

def enter_credentials(page, username, password):
    page.goto("https://generalssb-prod.ec.royalholloway.ac.uk/BannerExtensibility/customPage/page/RHUL_Attendance_Student")
    time.sleep(2)
    page.fill("xpath=//*[@id=\"i0116\"]", username + "@live.rhul.ac.uk")
    page.click("xpath=//*[@id=\"idSIButton9\"]")
    time.sleep(2)
    page.fill("xpath=//*[@id=\"i0118\"]", password)
    page.click("xpath=//*[@id=\"idSIButton9\"]")

    os.system("cls")

def get_credentials():
    username = input("Enter your username (xxxxyyy): ")
    password = input("Enter your password: ")
    save_credentials = input("Would you like to save your credentials for next time? (y/n): ")
    if save_credentials == "n":
        return username, password

    credentials = open("credentials.txt", "w")
    credentials.write(username + "\n" + password)
    credentials.close()
    return username, password

def check_existing_credentials():
    if os.path.exists("credentials.txt"):
        use_credentials = input("Do you want to use saved credentials? (y/n): ")
        if use_credentials == "y":
            credentials = open("credentials.txt", "r")
            username = credentials.readline().strip()
            password = credentials.readline().strip()
            credentials.close()
            return username, password
    return None, None

def retrieve_credentials():
    username, password = check_existing_credentials()
    if username is not None and password is not None:
        return username, password
    
    return get_credentials()

def microsoft_login(page):
    username, password = retrieve_credentials()
    enter_credentials(page, username, password)
    wait_for_verification(page)
