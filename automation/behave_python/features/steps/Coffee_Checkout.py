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

@given('Sonic web page is opened__CF')
def step_given_on_menu_page(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')
    print("Opened Sonic web page")

@when('I click on the "Drinks" category_CF')
def step_when_click_drinks(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]'
    print(f"Trying to find drinks element with selector: {drinks_selector}")
    drinks_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    assert drinks_element is not None, "Drinks element not found"
    drinks_element.click()
    print("Clicked on Drinks category")
    time.sleep(2)  # Give the page some time to load

@when('I click on the "Coffee" subcategory')
def step_when_click_subcategory(context):
    subcategory_selector = 'a[aria-labelledby="instructions-coffee"]'
    print(f"Trying to find subcategory element with selector: {subcategory_selector}")
    subcategory_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, subcategory_selector))
    )
    assert subcategory_element is not None, "Subcategory element 'Coffee' not found"
    subcategory_element.click()
    print("Clicked on Coffee subcategory")
    time.sleep(2)  # Give the page some time to load

@when('I open the drink product "Original Cold Brew Iced Coffee"')
def step_when_open_original_cold_brew_iced_coffee(context):
    product_selector = '//a[@href="/menu/drinks/coffee/original-cold-brew-iced-coffee/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    assert product_element is not None, "Drink product 'Original Cold Brew Iced Coffee' not found"
    product_element.click()
    print("Opened drink product 'Original Cold Brew Iced Coffee'")
    time.sleep(2)  # Give the page some time to load

@when('I open the drink product "French Vanilla Cold Brew Iced Coffee"')
def step_when_open_french_vanilla_cold_brew_iced_coffee(context):
    product_selector = '//a[@href="/menu/drinks/coffee/french-vanilla-cold-brew-iced-coffee/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    assert product_element is not None, "Drink product 'French Vanilla Cold Brew Iced Coffee' not found"
    product_element.click()
    print("Opened drink product 'French Vanilla Cold Brew Iced Coffee'")
    time.sleep(2)  # Give the page some time to load

@when('I open the drink product "Coffee"')
def step_when_open_coffee(context):
    product_selector = '//a[@href="/menu/drinks/coffee/coffee/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    assert product_element is not None, "Drink product 'Coffee' not found"
    product_element.click()
    print("Opened drink product 'Coffee'")
    time.sleep(2)  # Give the page some time to load

@when('I add the drink to the bag_CF')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    assert add_to_bag_button is not None, "Add to Bag button not found"
    add_to_bag_button.click()
    print("Added drink to the bag")
    time.sleep(2)  # Give the page some time to load

@when('I add all sizes of the drink to the bag_CF')
def step_when_add_all_sizes_to_bag(context):
    sizes = context.browser.find_elements(By.CSS_SELECTOR, 'div.sdi_productBanner_sizeSelectionWrapper__JwfQ5 button')
    assert sizes, "No sizes found for the product"
    print("Product has multiple sizes")
    for index, size in enumerate(sizes):
        size_text = size.text
        size.click()
        print(f"Selected size: {size_text}")
        add_to_bag_button = WebDriverWait(context.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
        )
        assert add_to_bag_button is not None, "Add to Bag button not found"
        add_to_bag_button.click()
        print(f"Added size {size_text} to the bag")
        time.sleep(2)  # Give the page some time to load
        if index < len(sizes) - 1:
            close_bag_button = WebDriverWait(context.browser, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
            )
            assert close_bag_button is not None, "Close Bag button not found"
            close_bag_button.click()
            print("Closed the bag")
            time.sleep(2)  # Give the page some time to load

@then('I remove all sizes of the drink from the bag_CF')
def step_then_remove_all_sizes_from_bag(context):
    remove_buttons = context.browser.find_elements(By.XPATH, "//button[@aria-label='remove bag item']")
    for remove_button in remove_buttons:
        remove_button.click()
        print("Removed a size from the bag")
        time.sleep(1)  # Give the page some time to update

@when('I proceed to checkout_CF')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    assert checkout_button is not None, "Checkout button not found"
    checkout_button.click()
    print("Proceeded to checkout")
    time.sleep(2)  # Give the page some time to load

@then('I should be on the checkout page_CF')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"
    print("Verified that we are on the checkout page")

@then('I click on the back button_CF')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    assert back_button is not None, "Back button not found"
    back_button.click()
    print("Clicked on the back button")
    time.sleep(2)  # Give the page some time to load

@then('I remove the drink from the bag_CF')
def step_then_remove_drink_from_bag(context):
    remove_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    assert remove_button is not None, "Remove button not found"
    remove_button.click()
    print("Removed the drink from the bag")
    time.sleep(1)  # Give the page some time to update

@then('I close the bag_CF')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    assert close_button is not None, "Close Bag button not found"
    close_button.click()
    print("Closed the bag")
    time.sleep(1)  # Give the page some time to update