from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()

@given('Sonic web page is opened__F')
def step_given_on_menu_page(context):
    context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')

@when('I click on the "Featured" category')
def step_when_click_featured(context):
    featured_selector = 'a[aria-labelledby="instructions-featured"]'
    featured_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, featured_selector))
    )
    featured_element.click()

@when('I scroll down to "{subcategory}"')
def step_impl(context, subcategory):
    subcategory_selector = f'//h2[text()="{subcategory}"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)

@when('I open the featured item "{item_name}"')
def step_impl(context, item_name):
    item_selector = f'//span[text()="{item_name}"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
    time.sleep(5)

@when('I add the featured item to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I proceed to checkout_F')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_F')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_F')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove the featured item from the bag')
def step_then_remove_featured_from_bag(context):
    remove_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_F')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()