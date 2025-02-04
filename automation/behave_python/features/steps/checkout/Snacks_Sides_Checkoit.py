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

@given('Sonic web page is opened_S')
def step_given_on_menu_page(context):
    context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')
    #context.browser.get('https://www.sonicdrivein.com/?locationId=6273')

@when('I click on the "Snacks & Sides" category')
def step_when_click_snacks_sides(context):
    category_selector = 'a[aria-labelledby="instructions-snacks-sides"]'
    category_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, category_selector))
    )
    category_element.click()

 # Steps for specific products
@when('I open the Snacks & Sides item "Mozzarella Sticks"')
def step_when_open_mozzarella_sticks(context):
    item_selector = '//a[@href="/menu/snacks-sides/mozzarella-sticks/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Groovy Fries"')
def step_when_open_groovy_fries(context):
    item_selector = '//a[@href="/menu/snacks-sides/groovy-fries/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()

@when('I open the Snacks & Sides item "Tots"')
def step_when_open_tots(context):
    item_selector = '//a[@href="/menu/snacks-sides/tots/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Chili Cheese Tots"')
def step_when_open_chili_cheese_tots(context):
    item_selector = '//a[@href="/menu/snacks-sides/chili-cheese-tots/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Ched \'R\' Peppers"')
def step_when_open_ched_r_peppers(context):
    item_selector = '//a[@href="/menu/snacks-sides/ched-r-peppers/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Onion Rings"')
def step_when_open_onion_rings(context):
    item_selector = '//a[@href="/menu/snacks-sides/onion-rings/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Pickle Fries"')
def step_when_open_pickle_fries(context):
    item_selector = '//a[@href="/menu/snacks-sides/pickle-fries/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Cheese Tots"')
def step_when_open_cheese_tots(context):
    item_selector = '//a[@href="/menu/snacks-sides/cheese-tots/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Chili Cheese Groovy Fries"')
def step_when_open_chili_cheese_groovy_fries(context):
    item_selector = '//a[@href="/menu/snacks-sides/chili-cheese-groovy-fries/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Cheese Groovy Fries"')
def step_when_open_cheese_groovy_fries(context):
    item_selector = '//a[@href="/menu/snacks-sides/cheese-groovy-fries/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I open the Snacks & Sides item "Side of Queso"')
def step_when_open_side_of_queso(context):
    item_selector = '//a[@href="/menu/snacks-sides/side-of-queso/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
 # Steps for scrolling and opening specific products
@when('I scroll down to Snacks and open the Snacks & Sides item "Corn Dog"')
def step_when_scroll_and_open_corn_dog(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/corn-dog/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I scroll down to Snacks and open the Snacks & Sides item "Soft Pretzel Twist"')
def step_when_scroll_and_open_soft_pretzel_twist(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/soft-pretzel-twist/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I scroll down to Snacks and open the Snacks & Sides item "Premium Chicken Bites"')
def step_when_scroll_and_open_premium_chicken_bites(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/premium-chicken-bites/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I scroll down to Snacks and open the Snacks & Sides item "Bacon Ranch Queso Wrap"')
def step_when_scroll_and_open_bacon_ranch_queso_wrap(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/bacon-ranch-queso-wrap/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I scroll down to Snacks and open the Snacks & Sides item "Southwest Crunch Queso Wrap"')
def step_when_scroll_and_open_southwest_crunch_queso_wrap(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/southwest-crunch-queso-wrap/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I scroll down to Snacks and open the Snacks & Sides item "FRITOS® Chili Cheese Jr. Wrap"')
def step_when_scroll_and_open_fritos_chili_cheese_jr_wrap(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/fritos-chili-cheese-jr-wrap/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I scroll down to Snacks and open the Snacks & Sides item "FRITOS® Chili Cheese Wrap"')
def step_when_scroll_and_open_fritos_chili_cheese_wrap(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/fritos-chili-cheese-wrap/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I scroll down to Snacks and open the Snacks & Sides item "FRITOS® Chili Pie"')
def step_when_scroll_and_open_fritos_chili_pie(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/fritos-chili-pie/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()
 
@when('I scroll down to Snacks and open the Snacks & Sides item "Ched \'R\' Bites"')
def step_when_scroll_and_open_ched_r_bites(context):
    subcategory_selector = '//h2[@data-testid="Snacks"]'
    subcategory_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, subcategory_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView();", subcategory_element)
    time.sleep(2)
    item_selector = '//a[@href="/menu/snacks-sides/ched-r-bites/"]'
    item_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, item_selector))
    )
    item_element.click()

@when('I add Snacks & Sides to the bag')
def step_when_add_to_bag(context):
    add_to_bag_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']"))
    )
    add_to_bag_button.click()

@when('I proceed to checkout_S')
def step_when_proceed_to_checkout(context):
    checkout_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
    )
    checkout_button.click()

@then('I should be on the checkout page_S')
def step_then_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout_paymentHeaderContainer__1I3zU"))
    )
    assert 'checkout' in context.browser.current_url, "Unable to open the checkout page"

@then('I click on the back button_S')
def step_then_click_back_button(context):
    back_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.paymentHeader_backContainer__IE_5k"))
    )
    back_button.click()

@then('I remove Snacks & Sides from the bag')
def step_then_remove_from_bag(context):
    remove_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='remove bag item']"))
    )
    remove_button.click()

@then('I close the bag_S')
def step_then_close_bag(context):
    close_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bag_closeButton__F5CVN"))
    )
    close_button.click()


@when('I add all sizes of Snacks & Sides to the bag')
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


@then('I remove all sizes of Snacks & Sides from the bag')
def step_then_remove_all_sizes_from_bag(context):
    remove_buttons = context.browser.find_elements(By.XPATH, "//button[@aria-label='remove bag item']")
    for remove_button in remove_buttons:
        remove_button.click()