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

@given('Sonic web page is opened_C')
def step_given_on_menu_page(context):
    #context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8811')

@when('I click on the "Carhop Classics" category')
def step_when_click_carhop_classics(context):
    category_selector = 'a[aria-labelledby="instructions-carhop-classics"]'
    category_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, category_selector))
    )
    category_element.click()

# Steps for specific products in Carhop Classics
@when('I open the Carhop Classics item "Quarter Pound Double Cheeseburger"')
def step_when_open_quarter_pound_double_cheeseburger(context):
    item_selector = '//a[@href="/menu/carhop-classics/quarter-pound-double-cheeseburger/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()

@when('I open the Carhop Classics item "FRITOS® Chili Cheese Wrap"')
def step_when_open_fritos_chili_cheese_wrap(context):
    item_selector = '//a[@href="/menu/carhop-classics/regular-fritos-chili-cheese-wrap/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()

@when('I open the Carhop Classics item "Grilled Cheese Sandwich"')
def step_when_open_grilled_cheese_sandwich(context):
    item_selector = '//a[@href="/menu/carhop-classics/grilled-cheese-sandwich/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()

@when('I open the Carhop Classics item "Premium Chicken Bites"')
def step_when_open_premium_chicken_bites(context):
    item_selector = '//a[@href="/menu/carhop-classics/premium-chicken-bites/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()

@when('I add Carhop Classics to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I proceed to checkout_C')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_C')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_C')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove Carhop Classics from the bag')
def step_then_remove_from_bag(context):
    remove_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_C')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()