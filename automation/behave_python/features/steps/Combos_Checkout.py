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

@given('Sonic web page is opened_Co')
def step_given_on_menu_page(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')

@when('I click on the "Combos" category')
def step_when_click_combos(context):
    category_selector = 'a[aria-labelledby="instructions-combos"]'
    category_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, category_selector))
    )
    category_element.click()

@when('I open the Combos product "{product_name}"')
def step_when_open_combos_product(context, product_name):
    product_selector = f'//span[@title="{product_name}"]/ancestor::a'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I click on the "Next" button')
def step_when_click_next_button(context):
    next_button_selector = '//button[contains(@class, "sdi_floatingBanner_nextBtn__0QFxD")]'
    next_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, next_button_selector))
    )
    next_button.click()

@when('I select the side item "{side_item}"')
def step_when_select_side_item(context, side_item):
    side_item_selector = f'//div[contains(@class, "sdi_verticalModifierCard_contentWrapper__0_Ytd")]//p[text()="{side_item}"]'
    side_item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, side_item_selector))
    )
    side_item_element.click()
 
@when('I select the drink "{drink}"')
def step_when_select_drink(context, drink):
    drink_selector = f'//div[contains(@class, "sdi_verticalModifierCard_contentWrapper__0_Ytd")]//p[text()="{drink}"]'
    drink_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, drink_selector))
    )
    drink_element.click()

@when('I add the Combos product to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I proceed to checkout_Co')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_Co')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_Co')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove the Combos product from the bag')
def step_then_remove_from_bag(context):
    remove_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_Co')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()