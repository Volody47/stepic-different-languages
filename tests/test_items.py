import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_web_page_has_button_add_to_basket(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    unic_button = button.get_attribute("class")
    assert unic_button == "btn btn-lg btn-primary btn-add-to-basket", "Кнопки нет на странице The button 'add to basket' doesn't exist"
