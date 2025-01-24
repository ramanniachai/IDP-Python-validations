from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.cookies_handled = False

def after_all(context):
    context.browser.quit()

@given('Sonic web page is opened_D')
def step_given_on_menu_page(context):
    #context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')

@given('I reject non-essential cookies and accept the privacy policy if needed_D')
def step_when_reject_cookies_if_needed(context):
    if not context.cookies_handled:
        try:
            WebDriverWait(context.browser, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Reject Non-Essential"]'))
            ).click()
        except:
            pass  # If the pop-up doesn't appear, continue
 
        try:
            WebDriverWait(context.browser, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.cookieBanner_closeButton__L4JiG'))
            ).click()
        except:
            pass  # If the pop-up doesn't appear, continue
 
        context.cookies_handled = True

@when('I click on the "Drinks" category')
def step_when_click_drinks(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]'
    drinks_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()

@when('I click on the "{subcategory}" subcategory')
def step_when_click_subcategory(context, subcategory):
    subcategory_selector = f'a[aria-labelledby="instructions-{subcategory.lower().replace(" ", "-")}"]'
    subcategory_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, subcategory_selector))
    )
    subcategory_element.click()

@when('I open the drink product at index {index}')
def step_when_open_drink_at_index(context, index):
    drink_selector = f"div[data-gtm-id='productItem']:nth-child({index}) a"
    drink_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drink_selector))
    )
    drink_element.click()

@when('I add the drink to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I proceed to checkout_D')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_D')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_D')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove the drink from the bag')
def step_then_remove_drink_from_bag(context):
    remove_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_D')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()