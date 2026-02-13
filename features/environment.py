from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """


    # ==================================================
    # =============== CHROME NORMAL MODE ===============
    # ==================================================


    chrome_options = ChromeOptions()

    chrome_driver_path = ChromeDriverManager().install()
    chrome_service = ChromeService(chrome_driver_path)

    context.driver = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    context.driver.maximize_window()


    # ==================================================
    # =============== CHROME HEADLESS ==================
    # ==================================================
    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")

    chrome_driver_path = ChromeDriverManager().install()
    chrome_service = ChromeService(chrome_driver_path)

    context.driver = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    """

    # ==================================================
    # =============== FIREFOX HEADLESS =================
    # ==================================================

    """
    firefox_options = FirefoxOptions()
    firefox_options.headless = True
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")

    firefox_driver_path = GeckoDriverManager().install()
    firefox_service = FirefoxService(firefox_driver_path)

    context.driver = webdriver.Firefox(
        service=firefox_service,
        options=firefox_options
    )
    """

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    context.driver.quit()