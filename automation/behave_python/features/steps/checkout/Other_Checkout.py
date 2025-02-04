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

@given('Sonic web page is opened__OT')
def step_given_on_menu_page(context):
    #context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')

@when('I click on the "Drinks" category_OT')
def step_when_click_drinks(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]'
    drinks_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()

@when('I click on the "Other" subcategory')
def step_when_click_subcategory(context):
    subcategory_selector = 'a[aria-labelledby="instructions-other"]'
    subcategory_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, subcategory_selector))
    )
    subcategory_element.click()

@when('I open the drink product "Red Bull Energy Drink"')
def step_when_open_red_bull_energy_drink(context):
    product_selector = '//a[@href="/menu/drinks/other/red-bull-energy-drink/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Water"')
def step_when_open_water(context):
    product_selector = '//a[@href="/menu/drinks/other/water/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Minute Maid® 100% Apple Juice Box"')
def step_when_open_minute_maid_apple_juice_box(context):
    product_selector = '//a[@href="/menu/drinks/other/minute-maid-100-apple-juice-box/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Milk Jug (1%) - White"')
def step_when_open_milk_jug_white(context):
    product_selector = '//a[@href="/menu/drinks/other/milk-jug-1-white/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Cup Of Ice"')
def step_when_open_cup_of_ice(context):
    product_selector = '//a[@href="/menu/drinks/other/cup-of-ice/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Orange Juice"')
def step_when_open_orange_juice(context):
    product_selector = '//a[@href="/menu/drinks/other/orange-juice/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I add the drink to the bag_OT')
def step_when_add_to_bag_ot(context):
    add_to_bag_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I add all sizes of the drink to the bag_OT')
def step_when_add_all_sizes_to_bag(context):
    sizes = context.browser.find_elements(By.CSS_SELECTOR, 'div.sdi_productBanner_sizeSelectionWrapper__JwfQ5 button')
    for index, size in enumerate(sizes):
        size.click()
        add_to_bag_button = WebDriverWait(context.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
        )
        add_to_bag_button.click()
        time.sleep(1)  # Give the page some time to load
        if index < len(sizes) - 1:
            close_bag_button = WebDriverWait(context.browser, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
            )
            close_bag_button.click()
            time.sleep(1)  # Give the page some time to load

@then('I remove all sizes of the drink from the bag_OT')
def step_then_remove_all_sizes_from_bag_ot(context):
    remove_buttons = context.browser.find_elements(By.XPATH, "//button[@aria-label='remove bag item']")
    for remove_button in remove_buttons:
        remove_button.click()

@when('I proceed to checkout_OT')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_OT')
def step_then_on_checkout_page_ot(context):
    WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_OT')
def step_then_click_back_button_ot(context):
    back_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove the drink from the bag_OT')
def step_then_remove_drink_from_bag_ot(context):
    remove_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_OT')
def step_then_close_bag_ot(context):
    close_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()