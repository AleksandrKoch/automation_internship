from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options  # used for BrowserStack capabilities

from app.application import Application


def browser_init(context, scenario_name):
    """
    BrowserStack Mobile session (real device)
    """

    bs_user = 'alexanderkoch_1j39IF'
    bs_key = 'pmkJzr43pXhsTUzfAUjh'

    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()

    #Disable Chrome notifications
    chrome_prefs = {
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", chrome_prefs)
    bstack_options = {

        # ===== Required BrowserStack options =====
        "sessionName": scenario_name,
        "projectName": "reelly_testing_2026",
        "buildName": "mobile-smoke",

        # ===== Mobile device settings =====
        # Pick ONE of these device examples (change as you need)
        "deviceName": "Google Pixel 7",
        "osVersion": "13",

        # ===== Debugging artifacts (highly recommended) =====
        "debug": True,                 # screenshots + logs in BS dashboard
        "networkLogs": True,
        "consoleLogs": "info",
    }

    # BrowserStack uses "bstack:options"
    options.set_capability("bstack:options", bstack_options)

    # Important: for mobile web, set browserName
    options.set_capability("browserName", "chrome")

    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    context.driver.quit()