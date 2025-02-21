import os
import logging
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from appium import webdriver as appium_webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import urllib3

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def before_all(context):
    steps_dir = os.path.join(os.path.dirname(__file__), 'steps')
    for root, dirs, files in os.walk(steps_dir):
        sys.path.append(root)
    logger.info(f"Added the following paths to Python path: {sys.path}")



    # Determine the testing environment from the TEST_ENV environment variable
    test_env = os.getenv('TEST_ENV', 'web').lower()
    
    if test_env == 'web':
        # Web testing setup
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--incognito")
        # Uncomment the next line if you need headless mode
        # chrome_options.add_argument("--headless")
        context.browser = webdriver.Chrome(options=chrome_options)
        context.browser.maximize_window()
        context.cookies_handled = False
        logger.info("Web environment setup completed.")
    elif test_env == 'app':
        # App testing setup
        try:
            options = UiAutomator2Options()
            options.set_capability('platformName', 'Android')
            options.set_capability('automationName', 'UiAutomator2')
            options.set_capability('deviceName', 'Pixel_7_Pro_API_35')
            options.set_capability('platformVersion', '15')
            options.set_capability('appPackage', 'com.snc.reactive.automationuat')
            options.set_capability('appActivity', 'com.inspirebrandsapp.MainActivity')
            options.set_capability('noReset', True)
            options.set_capability('adbExecTimeout', '30000')
            appium_server_url = 'http://127.0.0.1:4723'
            context.driver = appium_webdriver.Remote(appium_server_url, options=options)
            logger.info("App environment setup completed.")
        except Exception as e:
            logger.error(f"Error initializing Appium driver: {e}")
            context.driver = None
    else:
        raise ValueError(f"Unsupported TEST_ENV: {test_env}")

def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()
        logger.info("Web browser closed.")
    if hasattr(context, 'driver'):
        context.driver.quit()
        logger.info("App driver session ended.")

def after_scenario(context, scenario):
    if os.getenv('TEST_ENV', 'web').lower() == 'web':
        # Example web cleanup action
        context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')
        #context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    elif hasattr(context, 'driver'):
        # Example app cleanup action
        time.sleep(5)
        try:
            context.driver.implicitly_wait(10)
            menu_button = WebDriverWait(context.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "menu tab"))
            )
            menu_button.click()
            logging.info("Navigated back to the menu page in app.")
        except Exception as e:
            logging.error(f"Failed to navigate back to the menu page in app: {e}")