from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('Sonic web page is opened_MS')
def step_given_sonic_web_page_opened(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')

@when('I click on the "Frozen Zone" category_MS')
def step_when_click_frozen_zone(context):
    frozen_zone_selector = 'a[aria-labelledby="instructions-frozen-zone"]'
    frozen_zone_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, frozen_zone_selector))
    )
    frozen_zone_element.click()

@when('I click on the "Master Shakes" subcategory')
def step_when_click_master_shakes(context):
    master_shakes_selector = 'a[aria-labelledby="instructions-master-shakes"]'
    master_shakes_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, master_shakes_selector))
    )
    master_shakes_element.click()

@when('I open the Master Shakes product "{product_name}"')
def step_when_open_master_shakes_product(context, product_name):
    product_selector = f'//span[@title="{product_name}"]/ancestor::a'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I add all sizes of the Master Shakes product to the bag')
def step_when_add_all_sizes_to_bag(context):
    sizes = context.browser.find_elements(By.CSS_SELECTOR, 'div.sdi_productBanner_sizeSelectionWrapper__JwfQ5 button')
    for index, size in enumerate(sizes):
        size_text = size.text
        size.click()
        add_to_bag_button = WebDriverWait(context.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
        )
        add_to_bag_button.click()
        time.sleep(2)  # Allow the page to process the addition
        if index < len(sizes) - 1:
            close_bag_button = WebDriverWait(context.browser, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
            )
            close_bag_button.click()
            time.sleep(2)  # Allow the page to reload for the next size

@when('I proceed to checkout_MS')
def step_when_proceed_to_checkout(context):
    try:
        # Wait for the "Checkout" button to appear and become clickable
        checkout_button = WebDriverWait(context.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
        )
        checkout_button.click()
    except Exception as e:
        # Log the error for debugging
        print(f"Error: Unable to locate or click the Checkout button. Exception: {e}")
        raise

@then('I should be on the checkout page_MS')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url.lower(), "Unable to open the checkout page"

@then('I click on the back button_MS')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove all sizes of the Master Shakes product from the bag')
def step_then_remove_all_sizes_from_bag(context):
    remove_buttons = context.browser.find_elements(By.XPATH, "//button[@aria-label='remove bag item']")
    for remove_button in remove_buttons:
        remove_button.click()

@then('I close the bag_MS')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()