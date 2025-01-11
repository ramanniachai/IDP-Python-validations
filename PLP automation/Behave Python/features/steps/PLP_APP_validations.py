
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

#from appium.webdriver.common.touch_action import TouchAction

@given('UAT app is launched')
def step_impl(context):
    pass

@when('User opens menu page')
def step_impl(context):
    context.driver.implicitly_wait(10)
    menu_button = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "menu tab"))
    )
    menu_button.click()
    time.sleep(5)

@when('User taps on Combos category')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        combos_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category COMBOS Container"))
        )
        print("Combos category element found and clicked.")
        combos_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Combos category element.")
        raise

def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all combos products is displayed on the screen")
def step_impl(context):
    expected_products = [
       'Bacon Deluxe Double SONIC® Smasher Combo', 'Bacon Deluxe Triple SONIC® Smasher Combo', "Triple SONIC® Smasher Combo", "Double SONIC® Smasher Combo", "Cheesy Bacon SONIC® Stack Combo", "Cheesy Bacon SuperSONIC® Stack Combo", 
        "Garlic Butter Bacon Cheeseburger C...", "Plain SONIC® Cheeseburger Combo", "SONIC® Cheeseburger Combo", "SuperSONIC® Double Cheeseburger C...",
        "SuperSONIC® Bacon Double Cheeseburger C...", "Chili Cheese Coney Combo", "All-American Hot Dog Combo", "Footlong Quarter Pound Coney Combo",
        "Premium Chicken Bites Combo", "3 Piece Crispy Tenders Combo", "5 Piece Crispy Tenders Combo", "Crispy Chicken Sandwich Combo",
        "Ultimate Meat & Cheese Breakfast Burrito™ Combo", "SuperSONIC® Breakfast Burrito Combo", "Bacon Breakfast Burrito Combo", "Sausage Breakfast Burrito Combo",
        "Bacon Breakfast TOASTER® Combo", "Sausage Breakfast TOASTER® Com...", "French Toast Sticks Combo", 'Crispy Tenders Dinner - 3 piece', 'Crispy Tenders Dinner - 3 piece', 'Crispy Tender Dinner - 5 piece', 'Crispy Tender Dinner - 5 piece'
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


@when('User taps on Drinks category')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        drinks_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category DRINKS Container"))
        )
        print("Drinks category element found and clicked.")
        drinks_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Drinks category element.")
        raise


@when('User taps on Flavorista Favorites subcategory')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        flavorista_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category Flavorista Favorites Container"))
        )
        print("Flavorista category element found and clicked.")
        flavorista_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Flavorista category element.")
        raise



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Flavorista Favorites products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Strawberry Shortcake Snowball Slush Float", "Sparkling Sugar Cookie Dr Pepper®", "Lemonade Cream Cooler", "Rainbow Slush", "Twisted Flamingo", 
        "Classic Cruiser", "Dirty Dr Pepper®", 'Sour Dragon Fruit Recharger with Red Bull®', 'Strawberry Fusion Fizz'
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



@when('User taps on Sonic Rechargers subcategory')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        revharger_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category SONIC Rechargers with Red Bull Container"))
        )
        print("Recharger category element found and clicked.")
        revharger_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Recharger category element.")
        raise



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Sonic Rechargers products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Twisted Lime Recharger with Red Bull®", "Blood Orange Recharger with Red Bull®", "Dragon Fruit Recharger with Red Bull®", 'Sour Dragon Fruit Recharger with Red Bull®'
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



@when('User taps on Slushes subcategory')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        slush_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category Slushes Container"))
        )
        print("Slushes category element found and clicked.")
        slush_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Slushes category element.")
        raise



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Slushes products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Cherry Slush", "Blue Raspberry Slush", "Blue Coconut Slush", "Grape Slush", "Cranberry Slush", "Peach Slush", "Mango Slush", "POWERADE® Mountain Berry Blast® Slush",
        "Cherry Limeade Slush", "Limeade Slush", "Lemonade Slush", "Strawberry Slush"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



@when('User taps on Lemonades & Limeades subcategory')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        lemonades_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category Lemonades & Limeades Container"))
        )
        print("Lemonades & Limeades category element found and clicked.")
        lemonades_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Lemonades & Limeades category element.")
        raise



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Lemonades & Limeades products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Cherry Limeade", "Diet Cherry Limeade", "Strawberry Limeade", "Cranberry Limeade", "Limeade", "Diet Limeade", "All Natural Lemonade"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")

@when('User taps on Soft Drinks subcategory')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category Soft Drinks Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Soft Drinks category element found and clicked.")
    soft_element.click()



def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Soft Drinks products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Coca-Cola®", "Diet Coke®", "Coca-Cola® Zero", "Dr Pepper®", "Diet Dr Pepper®", "BARQ'S® Root Beer", "Sprite®", "Sprite Zero®", "Hi-C® Fruit Punch",
        "Fanta® Orange", "POWERADE® Mountain Berry Blast® Drink", "Ocean Water®", "Canada Dry®", 'Big Red®', 'Big Red®', 'Sun Drop®', 'Sun Drop®', 'Mello Yello', 'Mello Yello'
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")
 

def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")

@when('User taps on Iced Tea subcategory')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category Iced Tea Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Iced Tea category element found and clicked.")
    soft_element.click()



def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Iced Tea products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Sweet Iced Tea", "Unsweet Iced Tea", "Half Sweet Tea / Half Lemonade", "Half Sweet Tea / Half Unsweet Tea", "Half Unsweet Tea / Half Lemonade"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")

@when('User taps on Coffee subcategory')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category Coffee Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Coffee category element found and clicked.")
    soft_element.click()


def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Coffee products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Original Cold Brew Iced Coffee", "French Vanilla Cold Brew Iced Coffee", "Coffee"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")


@when('User taps on Other subcategory')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category Other Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Iced Tea category element found and clicked.")
    soft_element.click()


def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Other products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Red Bull Energy Drink", "Water", "Minute Maid® 100% Apple Juice Box", "Milk Jug (1%) - White", "Cup Of Ice", "Orange Juice"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


@when('User taps on Burgers category')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        burger_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category BURGERS Container"))
        )
        print("Burgers category element found and clicked.")
        burger_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find BURGERS category element.")
        raise



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Burgers products is displayed on the screen")
def step_impl(context):
    expected_products = [
        'Bacon Deluxe Double SONIC® Smasher', 'Bacon Deluxe Triple SONIC® Smasher', "Triple SONIC® Smasher", "Double SONIC® Smasher", "Cheesy Bacon SONIC® Stack", "Cheesy Bacon SuperSONIC® Stack", "Garlic Butter Bacon Cheeseburger", 
        "SONIC® Cheeseburger", "Plain SONIC® Cheeseburger", "Quarter Pound Double Cheeseburger", "SuperSONIC® Double Cheeseburger", "SuperSONIC® Bacon Double Cheeseburger"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


@when('User taps on Featured category')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        featured_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category BURGERS Container"))
        )
        print("Featured category element found and clicked.")
        featured_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Featured category element.")
        raise



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Featured products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Double SONIC® Smasher", "Triple SONIC® Smasher", "Side of Queso", "Bacon Ranch Queso Wrap", 
        "Southwest Crunch Queso Wrap", 'Bacon Deluxe Double SONIC® Smasher', 'Bacon Deluxe Triple SONIC® Smasher', "Strawberry Shortcake Snowball Slush Float", 
        'Sour Dragon Fruit Recharger with Red Bull®', 'Strawberry Fusion Fizz'
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


@when('User taps on $1.99 category')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        dollar_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category $1.99 MENU Container"))
        )
        print("$1.99 category element found and clicked.")
        dollar_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find $1.99 category element.")
        raise



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all $1.99 products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Grilled Cheese Burger", "Tots", "Bacon Ranch Queso Wrap", "Southwest Crunch Queso Wrap", 
        "Small Blue Coconut Cream Slush", "Small Strawberry Cream Slush", "Small Blood Orange Cream Slush"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")


@when('User taps on Snacks & Sides category')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category SNACKS & SIDES Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Snacks & Sides category element found and clicked.")
    soft_element.click()



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Snacks & Sides products is displayed on the screen")
def step_impl(context):
    expected_products = [
       "Groovy Fries", "Mozzarella Sticks", "Tots", "Pickle Fries", "Chili Cheese Tots",
        "Cheese Tots", "Chili Cheese Groovy Fries", "Cheese Groovy Fries", "Ched 'R' Peppers", "Onion Rings", "Side of Queso", "Southwest Crunch Queso Wrap", "Bacon Ranch Queso Wrap",
        "FRITOS® Chili Pie", "Soft Pretzel Twist", "Premium Chicken Bites", "Corn Dog", "FRITOS® Chili Cheese Wrap", "FRITOS® Chili Cheese Jr. Wrap", "Ched 'R' Bites", "Ched 'R' Bites"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")


@when('User taps on Carhop Classics category')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category Carhop Classics Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Carhop Classics category element found and clicked.")
    soft_element.click()



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Carhop Classics products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Quarter Pound Double Cheeseburger", "FRITOS® Chili Cheese Wrap", "Grilled Cheese Sandwich", "Premium Chicken Bites"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")





def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")

@when('User taps on Frozen Zone category')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category FROZEN ZONE® Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Frozen Zone category element found and clicked.")
    soft_element.click()

@when('User taps on Sonic Blasts subcategory')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        blast_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category SONIC Blasts® Container"))
        )
        print("Sonic Blasts category element found and clicked.")
        blast_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Sonic Blasts category element.")
        raise


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Sonic Blasts products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "SONIC Blast® made with REESE’S® Peanut Butter Cups", "Chocolate Chip Cookie Dough Blast®", "SONIC Blast® made with M&M’S® Chocolate Candies", 
        "SONIC Blast® made with OREO® Cookie Pieces", "SONIC Blast® made with HEATH®", "Chocolate Chunk Brownie Blast", "Turtle Truffle Nut Blast" 
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



@when('User taps on Classic Shakes subcategory')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        classic_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category Classic Shakes Container"))
        )
        print("Classic Shakes category element found and clicked.")
        classic_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Classic Shakes category element.")
        raise


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Classic Shakes products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Strawberry Classic Shake", "Chocolate Classic Shake", "Banana Classic Shake", "Vanilla Classic Shake", "Peanut Butter Classic Shake", 
        "Hot Fudge Classic Shake", "Caramel Classic Shake"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



@when('User taps on Master Shakes subcategory')
def step_impl(context):
    context.driver.implicitly_wait(10)
    try:
        master_element = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Category Master Shakes® Container"))
        )
        print("Master Shakes category element found and clicked.")
        master_element.click()
    except TimeoutException:
        print("TimeoutException: Failed to find Master Shakes category element.")
        raise


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Master Shakes products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Strawberry Cheesecake Master Shake®", "Cheesecake Master Shake®", "OREO® Cheesecake Master Shake®", 
        "OREO® Chocolate Master Shake®", "OREO® Peanut Butter Master Shake"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")

@when('User taps on Sundaes subcategory')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category Sundaes & Cones Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Sundaes & Cones category element found and clicked.")
    soft_element.click()


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Sundaes products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Hot Fudge Sundae", "Caramel Sundae", "Strawberry Sundae", "Vanilla Cup"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")


@when('User taps on Hot Dogs category')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category HOT DOGS Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("HOT DOGS category element found and clicked.")
    soft_element.click()
    

def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Hot Dogs products is displayed on the screen")
def step_impl(context):
    expected_products = [
       "Chili Cheese Coney", "All-American Dog", "Footlong Quarter Pound Coney", "Corn Dog", "New York Dog", #"Chicago Dog",
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")


@when('User taps on Chicken category')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category CHICKEN Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("CHICKEN category element found and clicked.")
    soft_element.click()



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Chicken products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Southwest Crunch Queso Wrap", "Bacon Ranch Queso Wrap", "Premium Chicken Bites", "Crispy Tenders - 3 Piece", "Crispy Tenders - 5 Piece",
        "Crispy Chicken Sandwich", '3 Piece Crispy Tender Dinner', '3 Piece Crispy Tender Dinner', '5 Piece Crispy Tender Dinner', '5 Piece Crispy Tender Dinner'
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")

@when('User taps on Breakfast category')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category BREAKFAST Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("BREAKFAST category element found and clicked.")
    soft_element.click()



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Breakfast products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "French Toast Sticks", "Bacon BREAKFAST TOASTER®", "Sausage BREAKFAST TOASTER®", "Bacon Breakfast Burrito", "Sausage Breakfast Burrito",
        "SuperSONIC® Breakfast Burrito", "Ultimate Meat & Cheese Breakfast Burrito™", "Jr. Bacon, Egg and Cheese Breakfast Burrito",
        "Jr. Sausage, Egg and Cheese Breakfast Burrito", #"Bacon, Egg and Cheese Brioche Breakfast Sandwich", "Sausage, Egg and Cheese Brioche Breakfast Sandwich",
        "Original Cold Brew Iced Coffee", "French Vanilla Cold Brew Iced Coffee", "Coffee", 'Plain Bagel', 'Plain Bagel', 'Ham, Egg and Cheese Bagel', 'Ham, Egg and Cheese Bagel'
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")

@when('User taps on Wacky Pack Kids Meals category')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category WACKY PACK® KIDS MEALS Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("WACKY PACK® KIDS MEALS category element found and clicked.")
    soft_element.click()



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Wacky Pack Kids Meals products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Hamburger Wacky Pack®", "Crispy Tenders Wacky Pack®", "Hot Dog Wacky Pack®", "Corn Dog Wacky Pack®", "Grilled Cheese Wacky Pack®"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")


def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = int(screen_size['height'] * 0.9)
    end_y = int(screen_size['height'] * 0.1)
    driver.swipe(start_x, start_y, start_x, end_y, 1000)


def scroll_to_element(driver, by, value, max_scroll_attempts=5):
    attempts = 0
    while attempts < max_scroll_attempts:
        elements = driver.find_elements(by, value)
        for element in elements:
            if element.is_displayed():
                return element
        scroll_down(driver)
        attempts += 1
    raise NoSuchElementException(f"Element with {value} not found after {max_scroll_attempts} scrolls.")


@when('User taps on Sandwiches category')
def step_impl(context):
    by = AppiumBy.ACCESSIBILITY_ID
    value = "Category SANDWICHES Container"
    # Скролл до элемента перед его кликом
    soft_element = scroll_to_element(context.driver, by, value)
    print("Sandwiches category element found and clicked.")
    soft_element.click()



def scroll_down(driver):
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 0.9
    end_y = screen_size['height'] * 0.1

    driver.swipe(start_x, start_y, start_x, end_y, 500)

def find_product_elements(driver):
    all_products = []
    last_products = []
    scroll_attempts = 0
    max_scroll_attempts = 5

    while scroll_attempts < max_scroll_attempts:
        time.sleep(2)  # Wait for elements to load
        product_elements = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'productContainer')]")
        
        current_products = [element.get_attribute("content-desc").split(" - ", 1)[-1] for element in product_elements]
        all_products.extend([product for product in current_products if product not in all_products])
        
        if current_products == last_products:
            break
        
        last_products = current_products
        scroll_down(driver)
        scroll_attempts += 1

    return all_products

@then("The list of all Sandwiches products is displayed on the screen")
def step_impl(context):
    expected_products = [
        "Grilled Cheese Sandwich", "Crispy Chicken Sandwich", #"Philly Cheesesteak"
    ]
    
    found_products = find_product_elements(context.driver)
    
    print("Found products:", found_products)
    
    for product_name in expected_products:
        assert any(product_name in found_product for found_product in found_products), f"Product '{product_name}' is not displayed on the page"
    
    print("All expected products were found on the page.")

