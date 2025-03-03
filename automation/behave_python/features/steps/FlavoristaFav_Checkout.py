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

@given('Sonic web page is opened__FF')
def step_given_on_menu_page(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')


@when('I click on the "Drinks" category')
def step_when_click_drinks(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]'
    print(f"Trying to find drinks element with selector: {drinks_selector}")
    drinks_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()


@when('I click on the "Flavorista Favorites" subcategory')
def step_when_click_subcategory(context):
    subcategory_selector = 'a[aria-labelledby="instructions-flavorista-favorites"]'
    print(f"Trying to find subcategory element with selector: {subcategory_selector}")
    subcategory_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, subcategory_selector))
    )
    subcategory_element.click()

@when('I open the drink product "Strawberry Mangonada Slush"')
def step_when_open_strawberry_shortcake_snowball_slush_float(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/strawberry-mangonada-slush/"]'
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Strawberry Shortcake Snowball Slush Float"')
def step_when_open_strawberry_shortcake_snowball_slush_float(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/strawberry-shortcake-snowball-slush-float/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Strawberry Fusion Fizz"')
def step_when_open_strawberry_fusion_fizz(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/strawberry-fusion-fizz/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()

@when('I open the drink product "Sour Dragon Fruit Recharger with Red Bull®"')
def step_when_open_sour_dragon_fruit_recharger(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/sour-dragon-fruit-recharger/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Sparkling Sugar Cookie Dr Pepper®"')
def step_when_open_sparkling_sugar_cookie_dr_pepper(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/sparkling-sugar-cookie-dr-pepper/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Lemonade Cream Cooler"')
def step_when_open_lemonade_cream_cooler(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/lemonade-cream-cooler/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Rainbow Slush"')
def step_when_open_rainbow_slush(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/rainbow-slush/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Twisted Flamingo"')
def step_when_open_twisted_flamingo(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/twisted-flamingo/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I open the drink product "Dirty Dr Pepper®"')
def step_when_open_dirty_dr_pepper(context):
    product_selector = '//a[@href="/menu/drinks/flavorista-favorites/dirty-dr-pepper/"]'
    print(f"Trying to find drink product with selector: {product_selector}")
    product_element = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    )
    product_element.click()


@when('I add the drink to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()


@when('I add all sizes of the drink to the bag')
def step_when_add_all_sizes_to_bag(context):
    sizes = context.browser.find_elements(By.CSS_SELECTOR, 'div.sdi_productBanner_sizeSelectionWrapper__JwfQ5 button')
    for index, size in enumerate(sizes):
        size_text = size.text
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

@then('I remove all sizes of the drink from the bag')
def step_then_remove_all_sizes_from_bag(context):
    remove_buttons = context.browser.find_elements(By.XPATH, "//button[@aria-label='remove bag item']")
    for remove_button in remove_buttons:
        remove_button.click()


@when('I proceed to checkout_FF')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()


@then('I should be on the checkout page_FF')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_FF')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()


@then('I remove the drink from the bag')
def step_then_remove_drink_from_bag(context):
    remove_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()


@then('I close the bag_FF')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()
