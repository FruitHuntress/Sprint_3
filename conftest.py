import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locator

main_url = 'https://stellarburgers.nomoreparties.site'

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1200,600')

    browser = webdriver.Chrome(options=options, executable_path='C:/WebDriver/bin/chromedriver.exe')
    browser.get(main_url)

    yield browser
    browser.quit()

@pytest.fixture()
def login(driver):
    driver.find_element(By.XPATH, Locator.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_email)))
    driver.find_element(By.XPATH, Locator.authorization_email).send_keys('anna_krylova_8_123@yandex.ru')
    driver.find_element(By.XPATH, Locator.authorization_password).send_keys('randompass123')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_button)))
    driver.find_element(By.XPATH, Locator.authorization_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.constructor_title)))
    return driver