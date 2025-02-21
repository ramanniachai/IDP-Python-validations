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

@given('Sonic web page is opened__SD')
def step_given_on_menu_page(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')
    print("Opened Sonic web page")

@when('I click on the "Drinks" category_SD')
def step_when_click_drinks(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]'
    drinks_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()

@when('I click on the "Soft Drinks" subcategory')
def step_when_click_subcategory(context):
    subcategory_selector = 'a[aria-labelledby="instructions-soft-drinks"]'
    subcategory_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, subcategory_selector))
    )
    subcategory_element.click()

@when('I open the drink product "Coca-Cola®"')
def step_when_open_coca_cola(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/coca-cola/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Diet Coke®"')
def step_when_open_diet_coke(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/diet-coke/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Coca-Cola® Zero"')
def step_when_open_coca_cola_zero(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/coca-cola-zero/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Dr Pepper®"')
def step_when_open_dr_pepper(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/dr-pepper/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Diet Dr Pepper®"')
def step_when_open_diet_dr_pepper(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/diet-dr-pepper/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "BARQ\'S® Root Beer"')
def step_when_open_barqs_root_beer(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/barqs-root-beer/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Sprite®"')
def step_when_open_sprite(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/sprite/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Sprite Zero®"')
def step_when_open_sprite_zero(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/sprite-zero/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Hi-C® Fruit Punch"')
def step_when_open_hi_c_fruit_punch(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/hi-c-fruit-punch/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Fanta® Orange"')
def step_when_open_fanta_orange(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/fanta-orange/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "POWERADE® Mountain Berry Blast® Drink"')
def step_when_open_powerade_mountain_berry_blast_drink(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/powerade-mountain-berry-blast/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Ocean Water®"')
def step_when_open_ocean_water(context):
    product_selector = '//a[@href="/menu/drinks/soft-drinks/ocean-water/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I add the drink to the bag_SD')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I add all sizes of the drink to the bag_SD')
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

@then('I remove all sizes of the drink from the bag_SD')
def step_then_remove_all_sizes_from_bag(context):
    remove_buttons = context.browser.find_elements(By.XPATH, "//button[@aria-label='remove bag item']")
    for remove_button in remove_buttons:
        remove_button.click()

@when('I proceed to checkout_SD')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_SD')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_SD')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove the drink from the bag_SD')
def step_then_remove_drink_from_bag(context):
    remove_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_SD')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()