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

@given('Sonic web page is opened__SL')
def step_given_on_menu_page(context):
    #context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')
    print("Opened Sonic web page")

@when('I click on the "Drinks" category_SL')
def step_when_click_drinks(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]'
    drinks_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()

@when('I click on the "Slushes" subcategory')
def step_when_click_subcategory(context):
    subcategory_selector = 'a[aria-labelledby="instructions-slushes"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, subcategory_selector))
    )
    subcategory_element.click()

@when('I scroll to the "Real Fruit Slushes" subcategory')
def step_when_scroll_to_real_fruit_slushes(context):
    real_fruit_slushes_selector = '//h2[@data-testid="Real Fruit Slushes"]'
    real_fruit_slushes_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, real_fruit_slushes_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", real_fruit_slushes_element)

@when('I open the drink product "Cherry Slush"')
def step_when_open_cherry_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/cherry-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Blue Raspberry Slush"')
def step_when_open_blue_raspberry_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/blue-raspberry-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Blue Coconut Slush"')
def step_when_open_blue_coconut_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/blue-coconut-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Grape Slush"')
def step_when_open_grape_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/grape-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Cranberry Slush"')
def step_when_open_cranberry_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/cranberry-juice-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Peach Slush"')
def step_when_open_peach_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/peach-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Mango Slush"')
def step_when_open_mango_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/mango-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "POWERADE® Mountain Berry Blast® Slush"')
def step_when_open_powerade_mountain_berry_blast_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/powerade-mountain-berry-blast-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Cherry Limeade Slush"')
def step_when_open_cherry_limeade_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/cherry-limeade-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Limeade Slush"')
def step_when_open_limeade_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/limeade-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Lemonade Slush"')
def step_when_open_lemonade_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/lemonade-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Strawberry Slush"')
def step_when_open_strawberry_slush(context):
    product_selector = '//a[@href="/menu/drinks/slushes/strawberry-slush/"]'
    product_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I add the slush to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I add all sizes of the slush to the bag')
def step_when_add_all_sizes_to_bag(context):
    sizes = context.browser.find_elements(By.CSS_SELECTOR, 'div.sdi_productBanner_sizeSelectionWrapper__JwfQ5 button')
    for index, size in enumerate(sizes):
        size.click()
        add_to_bag_button = WebDriverWait(context.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
        )
        assert add_to_bag_button is not None, "Add to Bag button not found"
        add_to_bag_button.click()
        time.sleep(1)  # Give the page some time to load
        if index < len(sizes) - 1:
            close_bag_button = WebDriverWait(context.browser, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
            )
            assert close_bag_button is not None, "Close Bag button not found"
            close_bag_button.click()
            time.sleep(1)  # Give the page some time to load

@then('I remove all sizes of the slush from the bag')
def step_then_remove_all_sizes_from_bag(context):
    remove_buttons = context.browser.find_elements(By.XPATH, "//button[@aria-label='remove bag item']")
    for remove_button in remove_buttons:
        remove_button.click()

@when('I proceed to checkout_SL')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_SL')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_SL')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove the slush from the bag')
def step_then_remove_drink_from_bag(context):
    remove_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_SL')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()