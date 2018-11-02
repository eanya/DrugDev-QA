from selenium import webdriver
import os

def browser_type() -> object:
    test_browser: str = "chrome"
    return test_browser


def before_all(context):
    base_dir = os.getcwd().split("\\behave")[0]
    driver_firefox = base_dir + "\Drivers\geckodriverv0.19.1.exe"
    driver_chrome = base_dir + "\Drivers\chromedriver32.exe"

    if browser_type() == "firefox":
        context.browser = webdriver.Firefox(driver_firefox)
    elif browser_type() == "chrome":
        context.browser = webdriver.Chrome(driver_chrome)
        context.browser.maximize_window()
        context.browser.delete_all_cookies()

def after_all(context):
    context.browser.quit()

