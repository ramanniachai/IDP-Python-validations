from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
import time

@given('Sonic web page is opened_FS')
def step_given_sonic_web_page(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8811')

@when('I click on the "Sandwiches" category_FS')
def step_when_click_sandwiches(context):
    category_selector = 'a[aria-labelledby="instructions-sandwiches"]'
    category_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, category_selector))
    )
    category_element.click()

@when('I open the Sandwiches product "Fish Sandwich"')
def step_when_open_product(context):
    product_selector = '//a[@href="/menu/sandwiches/fish-sandwich/"]'
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, product_selector))
    ).click()

@when('I select Pickles intensity as "Easy"')
def step_when_select_mayo(context):
    # Ensure the page has loaded the necessary elements
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw')]"))
    )

    # First, locate the Mayo card more robustly
    pickles_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and contains(., 'Pickles')]"
    pickles_card_element = context.browser.find_element(By.XPATH, pickles_card_xpath)
    context.browser.execute_script("arguments[0].scrollIntoView(true);", pickles_card_element)

    # Then, find the 'Regular' button within this card
    regular_button_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]//span[contains(text(), 'Regular')]"
    regular_button_element = pickles_card_element.find_element(By.XPATH, regular_button_xpath)
    regular_button_element.click()

    # Wait for the dropdown to appear and select 'Easy'
    easy_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'Easy')]"
    easy_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, easy_option_xpath))
    )
    easy_option_element.click()


@when('I select Tartar Sauce intensity as "Extra"')
def step_when_select_pickles(context):
    # Ensure the page has loaded the necessary elements
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw')]"))
    )

    # Locate the Pickles card
    tartar_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and contains(., 'Tartar Sauce')]"
    tartar_card_element = context.browser.find_element(By.XPATH, tartar_card_xpath)
    context.browser.execute_script("arguments[0].scrollIntoView(true);", tartar_card_element)

    # Find the 'Regular' button within this card (assuming 'Regular' is a default or necessary step before selecting 'Extra')
    regular_button_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]//span[contains(text(), 'Regular')]"
    regular_button_element = tartar_card_element.find_element(By.XPATH, regular_button_xpath)
    regular_button_element.click()

    # Wait for the dropdown to appear and select 'Extra'
    extra_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'Extra')]"
    extra_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, extra_option_xpath))
    )
    extra_option_element.click()

@when('I select Tartar Sauce intensity as "Easy"')
def step_when_select_pickles(context):
    # Ensure the page has loaded the necessary elements
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw')]"))
    )

    # Locate the Pickles card
    tartar_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and contains(., 'Tartar Sauce')]"
    tartar_card_element = context.browser.find_element(By.XPATH, tartar_card_xpath)
    context.browser.execute_script("arguments[0].scrollIntoView(true);", tartar_card_element)

    # Find the 'Regular' button within this card (assuming 'Regular' is a default or necessary step before selecting 'Extra')
    regular_button_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]//span[contains(text(), 'Regular')]"
    regular_button_element = tartar_card_element.find_element(By.XPATH, regular_button_xpath)
    regular_button_element.click()

    # Wait for the dropdown to appear and select 'Extra'
    extra_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'Easy')]"
    extra_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, extra_option_xpath))
    )
    extra_option_element.click()

@when('I select Cheese Slice intensity as "Regular"')
def step_when_select_ketchup(context):
     # Scroll to the "Add Sauces" modifier group
    add_toppings_group_selector = "//div[contains(@class, 'selectionHeader_titleWrapper__bvcDQ') and .//h2[text()='Add Toppings']]"
    add_toppings_group_element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, add_toppings_group_selector))
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", add_toppings_group_element)
     
     # Click on the "+Add" button for Ketchup
    add_button_selector = "//div[contains(@class, 'sdi_verticalModifierCard_sizeSelector__nyWwB') and text()='+ Add']"
    element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, add_button_selector))
    )
    context.browser.execute_script("arguments[0].click();", element)  # Click on the "+Add" button using JavaScript

@when('I add the Sandwiches product to the bag_FS')
def step_when_add_to_bag(context):
    add_to_bag_selector = "//button[contains(text(), 'Add to Bag')]"
    element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, add_to_bag_selector))
    )
    context.browser.execute_script("arguments[0].click();", element)  # Click on the "Add to Bag" button using JavaScript

@when('I proceed to checkout_FS')
def step_when_proceed_to_checkout(context):
    checkout_selector = "//button[contains(text(), 'Checkout')]"
    element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, checkout_selector))
    )
    context.browser.execute_script("arguments[0].click();", element)  # Click on the "Checkout" button using JavaScript

@then('I should be on the checkout page_FS')
def step_then_should_be_on_checkout_page(context):
    WebDriverWait(context.browser, 20).until(
        #EC.url_contains("https://www.sonicdrivein.com/checkout/")
        EC.url_contains("https://cfsnc.uat.irb.digital/checkout/")
    )

@when('I select Lettuce intensity as "Easy"')
def step_when_select_lettuce(context):
    # Ensure the page has loaded the necessary elements
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw')]"))
    )

    # Locate the Lettuce card
    lettuce_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and .//p[contains(text(), 'Lettuce')]]"
    lettuce_card_element = context.browser.find_element(By.XPATH, lettuce_card_xpath)
    context.browser.execute_script("arguments[0].scrollIntoView(true);", lettuce_card_element)

    # Find the 'Regular' button within this card
    regular_button_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]//span[contains(text(), 'Regular')]"
    regular_button_element = lettuce_card_element.find_element(By.XPATH, regular_button_xpath)
    regular_button_element.click()

    # Wait for the dropdown to appear and select 'Easy'
    easy_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'Easy')]"
    easy_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, easy_option_xpath))
    )
    easy_option_element.click()

@when('I select Tartar Sauce intensity as "None"')
def step_when_select_tartar_sauce_none(context):
    # Ensure the page has loaded the necessary elements
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw')]"))
    )

    # Locate the Tartar Sauce card
    tartar_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and .//p[contains(text(), 'Tartar Sauce')]]"
    tartar_card_element = context.browser.find_element(By.XPATH, tartar_card_xpath)
    context.browser.execute_script("arguments[0].scrollIntoView(true);", tartar_card_element)

    # Click on the intensity selector to open the dropdown
    intensity_selector_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]"
    intensity_selector_element = WebDriverWait(tartar_card_element, 20).until(
        EC.element_to_be_clickable((By.XPATH, intensity_selector_xpath))
    )
    intensity_selector_element.click()

    # Wait for the dropdown to appear and select 'None'
    none_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'None')]"
    none_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, none_option_xpath))
    )
    none_option_element.click()

@when('I select Cheese Slice intensity as "Extra"')
def step_when_select_cheese_easy(context):
    # Locate the Cheese Slice card
    cheese_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and .//p[contains(text(), 'Cheese Slice')]]"
    cheese_card_element = WebDriverWait(context.browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, cheese_card_xpath))
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", cheese_card_element)

    # Click on the "+ Add" button to add Cheese Slice
    add_button_xpath = ".//div[contains(@class, 'sdi_verticalModifierCard_sizeSelector__nyWwB') and contains(text(), '+ Add')]"
    add_button_element = WebDriverWait(cheese_card_element, 20).until(
        EC.element_to_be_clickable((By.XPATH, add_button_xpath))
    )
    add_button_element.click()

    # Wait for the intensity selector to appear and then click it to open the dropdown
    intensity_selector_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]"
    intensity_selector_element = WebDriverWait(cheese_card_element, 20).until(
        EC.element_to_be_clickable((By.XPATH, intensity_selector_xpath))
    )
    intensity_selector_element.click()

    # Wait for the dropdown to appear and select 'Extra'
    easy_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'Extra')]"
    easy_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, easy_option_xpath))
    )
    easy_option_element.click()



@when('I select Lettuce intensity as "Extra"')
def step_when_select_lettuce_extra(context):
    lettuce_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and .//p[contains(text(), 'Lettuce')]]"
    lettuce_card_element = WebDriverWait(context.browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, lettuce_card_xpath))
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", lettuce_card_element)

    intensity_selector_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]"
    intensity_selector_element = WebDriverWait(lettuce_card_element, 20).until(
        EC.element_to_be_clickable((By.XPATH, intensity_selector_xpath))
    )
    intensity_selector_element.click()

    extra_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'Extra')]"
    extra_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, extra_option_xpath))
    )
    extra_option_element.click()

@when('I select Pickles intensity as "None"')
def step_when_select_pickles_none(context):
    pickles_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and contains(., 'Pickles')]"
    pickles_card_element = WebDriverWait(context.browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, pickles_card_xpath))
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", pickles_card_element)

    intensity_selector_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]"
    intensity_selector_element = WebDriverWait(pickles_card_element, 20).until(
        EC.element_to_be_clickable((By.XPATH, intensity_selector_xpath))
    )
    intensity_selector_element.click()

    none_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'None')]"
    none_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, none_option_xpath))
    )
    none_option_element.click()

@when('I select Lettuce intensity as "None"')
def step_when_select_lettuce_none(context):
    lettuce_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and .//p[contains(text(), 'Lettuce')]]"
    lettuce_card_element = WebDriverWait(context.browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, lettuce_card_xpath))
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", lettuce_card_element)

    intensity_selector_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]"
    intensity_selector_element = WebDriverWait(lettuce_card_element, 20).until(
        EC.element_to_be_clickable((By.XPATH, intensity_selector_xpath))
    )
    intensity_selector_element.click()

    none_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'None')]"
    none_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, none_option_xpath))
    )
    none_option_element.click()

@when('I select Pickles intensity as "Extra"')
def step_when_select_pickles_extra(context):
    pickles_card_xpath = "//div[contains(@class, 'sdi_verticalModifierCard_container__MWRVw') and contains(., 'Pickles')]"
    pickles_card_element = WebDriverWait(context.browser, 20).until(
        EC.visibility_of_element_located((By.XPATH, pickles_card_xpath))
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", pickles_card_element)

    intensity_selector_xpath = ".//div[contains(@class, 'intensitySelector_selector__6IhLe')]"
    intensity_selector_element = WebDriverWait(pickles_card_element, 20).until(
        EC.element_to_be_clickable((By.XPATH, intensity_selector_xpath))
    )
    intensity_selector_element.click()

    extra_option_xpath = "//div[contains(@class, 'intensitySelector_popperContent__gA1G7')]//span[contains(text(), 'Extra')]"
    extra_option_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, extra_option_xpath))
    )
    extra_option_element.click()
