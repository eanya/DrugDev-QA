from selenium import webdriver


def browser_type() -> object:
    test_browser: str = "chrome"
    return test_browser


def before_all(context):
    if browser_type() == "firefox":
        context.browser = webdriver.Firefox(executable_path="./Drivers/geckodriverv0.19.1.exe")
    elif browser_type() == "chrome":
        context.browser = webdriver.Chrome("./Drivers/chromedriver32.exe")
        context.browser.maximize_window()
        context.browser.delete_all_cookies()

def after_all(context):
    context.browser.quit()

