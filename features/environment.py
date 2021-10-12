from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
import os
from os import getcwd
from pages.drag_drop import drag_drop
def before_scenario (context,scenario):
    path = os.getcwd()
    print(path)
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maiximized")
    option.add_argument("headless")
    context.browser = webdriver.Chrome(executable_path=path+"\drivers\chromedriver.exe",chrome_options=option)


    context.dd = drag_drop(context.browser) # c est equivalent à context.dd = drag_drop(context.browser).drag()

def after_scenario (context,scenario):

    context.browser.quit()

def after_step(context, step):
    if step.status == "failed":
        context.browser.save_screenshot('c://b/screenshot.png')
        attach(
            context.browser.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG)
