from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

@given('Sonic web page is opened__')
def step_given_on_menu_page(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    #context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')

@when('I reject non-essential cookies and accept the privacy policy')
def step_when_reject_cookies(context):
    try:
        # Wait for the cookie pop-up and reject non-essential cookies
        WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Reject Non-Essential"]'))
        ).click()
    except:
        pass  # If the pop-up doesn't appear, continue

    try:
        # Accept the privacy policy
        WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.cookieBanner_closeButton__L4JiG'))
        ).click()
    except:
        pass  # If the pop-up doesn't appear, continue

@when('I click on the "Burgers" category')
def step_when_click_burgers(context):
    burger_selector = 'a[aria-labelledby="instructions-burgers"]'
    burger_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, burger_selector))
    )
    burger_element.click()

@when('I open the first burger product')
def step_when_open_first_burger(context):
    first_burger = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-gtm-id='productItem'] a"))
    )
    first_burger.click()

@when('I add the burger to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I proceed to checkout')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()
'''
@then('I should be on the checkout page')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        #EC.url_contains('https://www.sonicdrivein.com/checkout/')
        EC.url_contains('https://cfsnc.uat.irb.digital/checkout/')
    )

    # Wait for a specific element on the checkout page to ensure it's fully loaded
    # Replace 'selector-for-checkout-page-element' with an actual element identifier from the checkout page
    checkout_page_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.checkout-page'))  # Update this selector
    )

    assert 'https://cfsnc.uat.irb.digital/checkout/' in context.browser.current_url
    context.browser.quit()

'''
@then('I should be on the checkout page')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"
    