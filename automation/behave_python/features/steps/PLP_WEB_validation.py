from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver


@given('Sonic web page is opened_')
def step_impl(context):
    context.browser.get('https://www.sonicdrivein.com/?locationId=6273')
    #context.browser.get('https://cfsnc.uat.irb.digital/?locationId=8810')

    time.sleep(5)

    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.ketch-flex.ketch-flex-1.ketch-flex-col'))
    )
    
    # Обработка кнопки для отклонения несущественных куки
    try:
        reject_button = WebDriverWait(context.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Reject Non-Essential"]'))
        )
        reject_button.click()
        
        # Подтверждение, что всплывающее окно исчезло
        WebDriverWait(context.browser, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.ketch-flex'))
        )

        # Ждем появления баннера с информацией о политике конфиденциальности и кликаем OK
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'cookieBanner_banner__iir9f'))
        )

        ok_button = WebDriverWait(context.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.cookieBanner_closeButton__L4JiG'))
        )

        ok_button.click()
        
        # Подтверждение, что баннер с информацией о политике конфиденциальности исчез
        WebDriverWait(context.browser, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'cookieBanner_banner__iir9f'))
        )
    except Exception as e:
        print("Error handling cookies or privacy banner:", str(e))



@when('User clicks on Combos category')
def step_impl(context):
    time.sleep(5)
    cobmos_selector = 'a[aria-labelledby="instructions-combos"]' 
    combos_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, cobmos_selector))
    )
    combos_element.click()


@then("The list of all combos products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        'Bacon Deluxe Double SONIC® Smasher Combo', 'Bacon Deluxe Triple SONIC® Smasher Combo', "Triple SONIC® Smasher Combo", "Double SONIC® Smasher Combo", "Cheesy Bacon SONIC® Stack Combo", "Cheesy Bacon SuperSONIC® Stack Combo", 
        "Garlic Butter Bacon Cheeseburger Combo", "Plain SONIC® Cheeseburger Combo", "SONIC® Cheeseburger Combo", "SuperSONIC® Double Cheeseburger Combo",
        "SuperSONIC® Bacon Double Cheeseburger Combo", "Chili Cheese Coney Combo", "All-American Hot Dog Combo", "Footlong Quarter Pound Coney Combo",
        "Premium Chicken Bites Combo", "3 Piece Crispy Tenders Combo", "5 Piece Crispy Tenders Combo", "Crispy Chicken Sandwich Combo",
        "Ultimate Meat & Cheese Breakfast Burrito™ Combo", "SuperSONIC® Breakfast Burrito Combo", "Bacon Breakfast Burrito Combo", "Sausage Breakfast Burrito Combo",
        "Bacon Breakfast TOASTER® Combo", "Sausage Breakfast TOASTER® Combo", "French Toast Sticks Combo", 'Crispy Tenders Dinner - 3 piece', 'Crispy Tender Dinner - 5 piece',
        'Fish Sandwich Combo'
    ]
    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]


    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]

    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"



@when('User clicks on Drinks category')
def drinks_category_click(context):
    time.sleep(5)
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]' 
    drinks_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()


@when('User clicks on Flavorista Favorites subcategory')
def step_impl(context):
    time.sleep(5)
    flavFav_selector = 'a[aria-labelledby="instructions-flavorista-favorites"]' 
    flavFav_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, flavFav_selector))
    )
    flavFav_element.click()


@then("The list of all Flavorista Favorites products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
       "Strawberry Mangonada Slush","Strawberry Shortcake Snowball Slush Float", "Sparkling Sugar Cookie Dr Pepper®", "Lemonade Cream Cooler", "Rainbow Slush", "Twisted Flamingo", 
       "Dirty Dr Pepper®", 'Sour Dragon Fruit Recharger with Red Bull®', 'Strawberry Fusion Fizz'

    ]
    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"

'''
@when('User clicks on Drinks category')
def drinks_category_click1(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]' 
    drinks_element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()
'''

@when('User clicks on Sonic Rechargers subcategory')
def step_impl(context):
    time.sleep(5)
    rechargers_selector = 'a[aria-labelledby="instructions-sonic-rechargers-with-red-bull"]' 
    rechargers_element = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, rechargers_selector))
    )
    rechargers_element.click()


@then("The list of all Sonic Rechargers products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Twisted Lime Recharger with Red Bull®", "Blood Orange Recharger with Red Bull®", "Dragon Fruit Recharger with Red Bull®", 'Sour Dragon Fruit Recharger with Red Bull®'
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"
'''
@when('User clicks on Drinks category')
def drinks_category_click2(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]' 
    drinks_element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()
'''

@when('User clicks on Slushes subcategory')
def step_impl(context):
    time.sleep(5)
    slushes_selector = 'a[aria-labelledby="instructions-slushes"]' 
    slushes_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, slushes_selector))
    )
    slushes_element.click()


@then("The list of all Slushes products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Cherry Slush", "Blue Raspberry Slush", "Blue Coconut Slush", "Grape Slush", "Cranberry Slush", "Peach Slush", "Mango Slush", "POWERADE® Mountain Berry Blast® Slush",
        "Cherry Limeade Slush", "Limeade Slush", "Lemonade Slush", "Strawberry Slush"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


'''
@when('User clicks on Drinks category')
def drinks_category_click2(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]' 
    drinks_element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()
'''

@when('User clicks on Lemonades & Limeades subcategory')
def step_impl(context):
    time.sleep(5)
    lemonades_selector = 'a[aria-labelledby="instructions-lemonades-limeades"]' 
    lemonades_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, lemonades_selector))
    )
    lemonades_element.click()


@then("The list of all Lemonades & Limeades products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Cherry Limeade", "Diet Cherry Limeade", "Strawberry Limeade", "Cranberry Limeade", "Limeade", "Diet Limeade", "All Natural Lemonade"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"

'''
@when('User clicks on Drinks category')
def drinks_category_click3(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]' 
    drinks_element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()
'''

@when('User clicks on Soft Drinks subcategory')
def step_impl(context):
    time.sleep(5)
    softDrinks_selector = 'a[aria-labelledby="instructions-soft-drinks"]' 
    softDrinks_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, softDrinks_selector))
    )
    softDrinks_element.click()


@then("The list of all Soft Drinks products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Coca-Cola®", "Diet Coke®", "Coca-Cola® Zero", "Dr Pepper®", "Diet Dr Pepper®", "BARQ'S® Root Beer", "Sprite®", "Sprite Zero®", "Hi-C® Fruit Punch",
        "Fanta® Orange", "POWERADE® Mountain Berry Blast® Drink", "Ocean Water®", "Canada Dry®", 'Big Red®', 'Big Red®', 'Sun Drop®', 'Sun Drop®', 'Mello Yello', 'Mello Yello'
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"

'''
@when('User clicks on Drinks category')
def drinks_category_click4(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]' 
    drinks_element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()
'''

@when('User clicks on Iced Tea subcategory')
def step_impl(context):
    time.sleep(5)
    icedTea_selector = 'a[aria-labelledby="instructions-iced-tea"]' 
    icedTea_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, icedTea_selector))
    )
    icedTea_element.click()


@then("The list of all Iced Tea products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Sweet Iced Tea", "Unsweet Iced Tea", "Half Sweet Tea / Half Lemonade", "Half Sweet Tea / Half Unsweet Tea", "Half Unsweet Tea / Half Lemonade"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"

'''
@when('User clicks on Drinks category')
def drinks_category_click5(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]' 
    drinks_element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()
'''

@when('User clicks on Coffee subcategory')
def step_impl(context):
    time.sleep(5)
    coffee_selector = 'a[aria-labelledby="instructions-coffee"]' 
    coffee_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, coffee_selector))
    )
    coffee_element.click()


@then("The list of all Coffee products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Original Cold Brew Iced Coffee", "French Vanilla Cold Brew Iced Coffee", "Coffee"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"

'''
@when('User clicks on Drinks category')
def drinks_category_click6(context):
    drinks_selector = 'a[aria-labelledby="instructions-drinks"]' 
    drinks_element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, drinks_selector))
    )
    drinks_element.click()
'''

@when('User clicks on Other subcategory')
def step_impl(context):
    time.sleep(5)
    other_selector = 'a[aria-labelledby="instructions-other"]' 
    other_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, other_selector))
    )
    other_element.click()


@then("The list of all Other products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Red Bull Energy Drink", "Water", "Minute Maid® 100% Apple Juice Box", "Milk Jug (1%) - White", "Cup Of Ice", "Orange Juice"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


@when('User clicks on Burgers category')
def step_impl(context):
    time.sleep(5)
    burger_selector = 'a[aria-labelledby="instructions-burgers"]' 
    burger_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, burger_selector))
    )
    burger_element.click()


@then("The list of all Burgers products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        'Bacon Deluxe Double SONIC® Smasher', 'Bacon Deluxe Triple SONIC® Smasher', "Triple SONIC® Smasher", "Double SONIC® Smasher", "Cheesy Bacon SONIC® Stack", "Cheesy Bacon SuperSONIC® Stack", "Garlic Butter Bacon Cheeseburger", 
        "SONIC® Cheeseburger", "Plain SONIC® Cheeseburger", "Quarter Pound Double Cheeseburger", "SuperSONIC® Double Cheeseburger", "SuperSONIC® Bacon Double Cheeseburger"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


@when('User clicks on Featured category')
def step_impl(context):
    time.sleep(5)
    featured_selector = 'a[aria-labelledby="instructions-featured"]' 
    featured_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, featured_selector))
    )
    featured_element.click()


@then("The list of all Featured products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Strawberry Mangonada Slush", "Double SONIC® Smasher", "Triple SONIC® Smasher", "Side of Queso", "Bacon Ranch Queso Wrap", 
        "Southwest Crunch Queso Wrap", 'Bacon Deluxe Double SONIC® Smasher', 'Bacon Deluxe Triple SONIC® Smasher', "Strawberry Shortcake Snowball Slush Float", 
        "Fish Sandwich" 
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__container__Qu3PO div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


@when('User clicks on $1.99 category')
def step_impl(context):
    time.sleep(5)
    dolNN_selector = 'a[aria-labelledby="instructions-value-menu"]' 
    dolNN_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, dolNN_selector))
    )
    dolNN_element.click()


@then("The list of all $1.99 products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Soft Pretzel Twist", "Bacon Ranch Queso Wrap", "Southwest Crunch Queso Wrap", "Jr. Deluxe Cheeseburger", "Small Coca-Cola® Float", 
        "Small Fanta® Orange Float", "Small Dr Pepper® Float", "Small BARQ’S® Root Beer Float", "French Toast Sticks"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


@when('User clicks on Snacks & Sides category')
def step_impl(context):
    time.sleep(5)
    snacksSides_selector = 'a[aria-labelledby="instructions-snacks-sides"]' 
    snacksSides_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, snacksSides_selector))
    )
    snacksSides_element.click()


@then("The list of all Snacks & Sides products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Groovy Fries", "Mozzarella Sticks", "Tots", "Pickle Fries", "Chili Cheese Tots",
        "Cheese Tots", "Chili Cheese Groovy Fries", "Cheese Groovy Fries", "Ched 'R' Peppers", "Onion Rings", "Side of Queso", "Southwest Crunch Queso Wrap", "Bacon Ranch Queso Wrap",
        "FRITOS® Chili Pie", "Soft Pretzel Twist", "Premium Chicken Bites", "Corn Dog", "FRITOS® Chili Cheese Wrap", "FRITOS® Chili Cheese Jr. Wrap", "Ched 'R' Bites", "Ched 'R' Bites"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"



@when('User clicks on Carhop Classics category')
def step_impl(context):
    time.sleep(5)
    carhop_selector = 'a[aria-labelledby="instructions-carhop-classics"]' 
    carhop_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, carhop_selector))
    )
    carhop_element.click()


@then("The list of all Carhop Classics products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Quarter Pound Double Cheeseburger", "FRITOS® Chili Cheese Wrap", "Grilled Cheese Sandwich", "Premium Chicken Bites"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"




@when('User clicks on Frozen Zone category')
def drinks_category_click3(context):
    time.sleep(5)
    frozenZone_selector = 'a[aria-labelledby="instructions-frozen-zone"]' 
    frozenZone_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, frozenZone_selector))
    )
    frozenZone_element.click()


@when('User clicks on Sonic Blasts subcategory')
def step_impl(context):
    time.sleep(5)
    sonicBl_selector = 'a[aria-labelledby="instructions-sonic-blasts"]' 
    sonicBl_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, sonicBl_selector))
    )
    sonicBl_element.click()


@then("The list of all Sonic Blasts products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "SONIC Blast® made with REESE’S® Peanut Butter Cups", "Chocolate Chip Cookie Dough Blast®", "SONIC Blast® made with M&M’S® Chocolate Candies", 
        "SONIC Blast® made with OREO® Cookie Pieces", "SONIC Blast® made with HEATH®", "Chocolate Chunk Brownie Blast", "Turtle Truffle Nut Blast"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


@when('User clicks on Classic Shakes subcategory')
def step_impl(context):
    time.sleep(5)
    classicShakes_selector = 'a[aria-labelledby="instructions-classic-shakes"]' 
    classicShakes_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, classicShakes_selector))
    )
    classicShakes_element.click()


@then("The list of all Classic Shakes products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Strawberry Classic Shake", "Chocolate Classic Shake", "Banana Classic Shake", "Vanilla Classic Shake", "Peanut Butter Classic Shake", 
        "Hot Fudge Classic Shake", "Caramel Classic Shake"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"

@when('User clicks on Master Shakes subcategory')
def step_impl(context):
    time.sleep(5)
    masterShakes_selector = 'a[aria-labelledby="instructions-master-shakes"]' 
    masterShakes_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, masterShakes_selector))
    )
    masterShakes_element.click()


@then("The list of all Master Shakes products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Strawberry Cheesecake Master Shake®", "Cheesecake Master Shake®", "OREO® Cheesecake Master Shake®", "OREO® Chocolate Master Shake®", 
        "OREO® Peanut Butter Master Shake"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


@when('User clicks on Sundaes subcategory')
def step_impl(context):
    time.sleep(5)
    sundaes_selector = 'a[aria-labelledby="instructions-sundaes-cones"]' 
    sundaes_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, sundaes_selector))
    )
    sundaes_element.click()


@then("The list of all Sundaes products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Hot Fudge Sundae", "Caramel Sundae", "Strawberry Sundae", "Vanilla Cup"
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"

@when('User clicks on Hot Dogs category')
def step_impl(context):
    time.sleep(5)
    hotDogs_selector = 'a[aria-labelledby="instructions-hot-dogs"]' 
    hotDogs_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, hotDogs_selector))
    )
    hotDogs_element.click()


@then("The list of all Hot Dogs products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Chili Cheese Coney", "All-American Dog", "Footlong Quarter Pound Coney", "Corn Dog", "New York Dog", #"Chicago Dog",
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


@when('User clicks on Chicken category')
def step_impl(context):
    time.sleep(5)
    chicken_selector = 'a[aria-labelledby="instructions-chicken"]' 
    chicken_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, chicken_selector))
    )
    chicken_element.click()


@then("The list of all Chicken products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Southwest Crunch Queso Wrap", "Bacon Ranch Queso Wrap", "Premium Chicken Bites", "Crispy Tenders - 3 Piece", "Crispy Tenders - 5 Piece",
        "Crispy Chicken Sandwich", '3 Piece Crispy Tender Dinner', '3 Piece Crispy Tender Dinner', '5 Piece Crispy Tender Dinner', '5 Piece Crispy Tender Dinner'
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"


@when('User clicks on Breakfast category')
def step_impl(context):
    time.sleep(5)
    breakfast_selector = 'a[aria-labelledby="instructions-breakfast"]' 
    breakfast_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, breakfast_selector))
    )
    breakfast_element.click()


@then("The list of all Breakfast products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "French Toast Sticks", "Bacon BREAKFAST TOASTER®", "Sausage BREAKFAST TOASTER®", "Bacon Breakfast Burrito", "Sausage Breakfast Burrito",
        "SuperSONIC® Breakfast Burrito", "Ultimate Meat & Cheese Breakfast Burrito™", "Jr. Bacon, Egg and Cheese Breakfast Burrito",
        "Jr. Sausage, Egg and Cheese Breakfast Burrito", #"Bacon, Egg and Cheese Brioche Breakfast Sandwich", "Sausage, Egg and Cheese Brioche Breakfast Sandwich",
        "Original Cold Brew Iced Coffee", "French Vanilla Cold Brew Iced Coffee", "Coffee", 'Plain Bagel', 'Plain Bagel', 'Ham, Egg and Cheese Bagel', 'Ham, Egg and Cheese Bagel'
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"



@when('User clicks on Wacky Pack category')
def step_impl(context):
    time.sleep(5)
    wackyPack_selector = 'a[aria-labelledby="instructions-wacky-pack-kids-meals"]' 
    wackyPack_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, wackyPack_selector))
    )
    wackyPack_element.click()


@then("The list of all Wacky Pack products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
        "Hamburger Wacky Pack®", "Crispy Tenders Wacky Pack®", "Hot Dog Wacky Pack®", "Corn Dog Wacky Pack®", "Grilled Cheese Wacky Pack®"
    ]
    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"



@when('User clicks on Sandwiches category')
def step_impl(context):
    time.sleep(5)
    sandwiches_selector = 'a[aria-labelledby="instructions-sandwiches"]' 
    sandwiches_element = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, sandwiches_selector))
    )
    sandwiches_element.click()


@then("The list of all Sandwiches products is displayed on the page")
def step_impl(context):
    time.sleep(5)
    expected_items = [
         "Grilled Cheese Sandwich", "Crispy Chicken Sandwich", "Fish Sandwich" 
    ]

    product_containers = WebDriverWait(context.browser, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._menuCategoryUrl__sectionItemsContainer__rtq1I div[data-gtm-id='productItem']"))
    )

    found_items = [
        container.find_element(By.CSS_SELECTOR, "span[data-testid='product-name']").text
        for container in product_containers
    ]

    missing_items = [item for item in expected_items if item not in found_items]
    excess_items = [item1 for item1 in found_items if item1 not in expected_items]
    assert not missing_items, f"Missing products on the page: {missing_items}"
    assert not excess_items, f"Unexpected products on the page: {excess_items}"