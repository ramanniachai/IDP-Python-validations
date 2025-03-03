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

@given('Sonic web page is opened__IT')
def step_given_on_menu_page(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')
    print("Opened Sonic web page")

@when('I click on the "Drinks" category_IT')
def step_when_click_drinks(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]'
    drinks_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()

@when('I click on the "Iced Tea" subcategory')
def step_when_click_subcategory(context):
    subcategory_selector = 'a[aria-labelledby="instructions-iced-tea"]'
    subcategory_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, subcategory_selector))
    )
    subcategory_element.click()

@when('I open the drink product "Sweet Iced Tea"')
def step_when_open_sweet_iced_tea(context):
    product_selector = '//a[@href="/menu/drinks/iced-tea/sweet-iced-tea/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Unsweet Iced Tea"')
def step_when_open_unsweet_iced_tea(context):
    product_selector = '//a[@href="/menu/drinks/iced-tea/unsweet-iced-tea/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Half Sweet Tea / Half Lemonade"')
def step_when_open_half_sweet_tea_half_lemonade(context):
    product_selector = '//a[@href="/menu/drinks/iced-tea/half-sweet-tea-half-lemonade/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Half Sweet Tea / Half Unsweet Tea"')
def step_when_open_half_sweet_tea_half_unsweet_tea(context):
    product_selector = '//a[@href="/menu/drinks/iced-tea/half-sweet-tea-half-unsweet-tea/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Half Unsweet Tea / Half Lemonade"')
def step_when_open_half_unsweet_tea_half_lemonade(context):
    product_selector = '//a[@href="/menu/drinks/iced-tea/half-unsweet-tea-half-lemonade/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I add the drink to the bag_IT')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I add all sizes of the drink to the bag_IT')
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

@then('I remove all sizes of the drink from the bag_IT')
def step_then_remove_all_sizes_from_bag(context):
    remove_buttons = context.browser.find_elements(By.XPATH, "//button[@aria-label='remove bag item']")
    for remove_button in remove_buttons:
        remove_button.click()

@when('I proceed to checkout_IT')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_IT')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_IT')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove the drink from the bag_IT')
def step_then_remove_drink_from_bag(context):
    remove_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_IT')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()