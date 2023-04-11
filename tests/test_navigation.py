from locator import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

unclicked_sauces = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
unclicked_buns = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
unclicked_toppings = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'

class TestProfileOpen:
    def test_profile_page_open(self, login):
        driver = login
        driver.find_element(By.XPATH, Locator.profile_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_link)))
        title = driver.find_element(By.XPATH, Locator.profile_link).text
        assert title == "Профиль"


    def test_from_profile_to_constructor_by_button(self, login):
        driver = login
        driver.find_element(By.XPATH, Locator.profile_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_link)))

        driver.find_element(By.XPATH, Locator.constructor_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.constructor_title)))
        title = driver.find_element(By.XPATH, Locator.constructor_title).text
        assert title == "Соберите бургер"

    def test_from_profile_to_constructor_by_logo(self, login):
        driver = login
        driver.find_element(By.XPATH, Locator.profile_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_link)))

        driver.find_element(By.XPATH, Locator.logo).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.constructor_title)))
        title = driver.find_element(By.XPATH, Locator.constructor_title).text
        assert title == "Соберите бургер"

    def test_constructor_to_sauces_navigation(self, login):
        driver = login

        driver.find_element(By.XPATH, Locator.sauces).click()
        clicked_sauces = driver.find_element(By.XPATH, Locator.sauces).get_attribute('class')
        assert clicked_sauces != unclicked_sauces

    def test_constructor_to_buns_navigation(self, login):
        driver = login

        driver.find_element(By.XPATH, Locator.sauces).click()
        driver.find_element(By.XPATH, Locator.buns).click()
        clicked_buns = driver.find_element(By.XPATH, Locator.buns).get_attribute('class')
        assert clicked_buns != unclicked_buns

    def test_constructor_to_toppings_navigation(self, login):
        driver = login

        driver.find_element(By.XPATH, Locator.toppings).click()
        clicked_toppings = driver.find_element(By.XPATH, Locator.toppings).get_attribute('class')
        assert clicked_toppings != unclicked_toppings




