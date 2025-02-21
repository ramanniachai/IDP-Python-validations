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

@given('Sonic web page is opened_SU')
def step_given_on_menu_page(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')
    print("Opened Sonic web page")

@when('I click on the "Frozen Zone" category_SU')
def step_when_click_frozen_zone(context):
    category_selector = 'a[aria-labelledby="instructions-frozen-zone"]'
    category_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, category_selector))
    )
    category_element.click()
    #time.sleep(2)  # Give the page some time to load

@when('I click on the "Sundaes" subcategory')
def step_when_click_subcategory(context):
    subcategory_selector = 'a[aria-labelledby="instructions-sundaes-cones"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, subcategory_selector))
    )
    subcategory_element.click()
    #time.sleep(2)  # Give the page some time to load

@when('I open the Sundaes product "{product_name}"')
def step_when_open_frozen_zone_product(context, product_name):
    product_selector = f'//span[@title="{product_name}"]/ancestor::a'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()
    #print(f"Opened Frozen Zone product '{product_name}'")
    #time.sleep(2)  # Give the page some time to load

@when('I add the Sundaes product to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    #assert add_to_bag_button is not None, "Add to Bag button not found"
    add_to_bag_button.click()
    #print("Added Frozen Zone product to the bag")
    #time.sleep(2)  # Give the page some time to load

@then('I remove the Sundaes product from the bag')
def step_then_remove_from_bag(context):
    remove_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    #assert remove_button is not None, "Remove button not found"
    remove_button.click()
    #print("Removed the Frozen Zone product from the bag")
    #time.sleep(1)  # Give the page some time to update

@when('I proceed to checkout_SU')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    #assert checkout_button is not None, "Checkout button not found"
    checkout_button.click()
    #print("Proceeded to checkout")
    #time.sleep(2)  # Give the page some time to load

@then('I should be on the checkout page_SU')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"
    #print("Verified that we are on the checkout page")

@then('I click on the back button_SU')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    #assert back_button is not None, "Back button not found"
    back_button.click()
    #print("Clicked on the back button")
    #time.sleep(2)  # Give the page some time to load

@then('I close the bag_SU')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    #assert close_button is not None, "Close Bag button not found"
    close_button.click()
    #print("Closed the bag")
    #time.sleep(1)  # Give the page some time to update