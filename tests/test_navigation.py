from locator import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestProfileOpen:
    def test_profile_page_open(self, login):
        login.find_element(By.XPATH, Locator.profile_button).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_link)))
        title = login.find_element(By.XPATH, Locator.profile_link).text
        assert title == "Профиль"


    def test_from_profile_to_constructor_by_button(self, login):
        login.find_element(By.XPATH, Locator.profile_button).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_link)))

        login.find_element(By.XPATH, Locator.constructor_button).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.constructor_title)))
        title = login.find_element(By.XPATH, Locator.constructor_title).text
        assert title == "Соберите бургер"

    def test_from_profile_to_constructor_by_logo(self, login):
        login.find_element(By.XPATH, Locator.profile_button).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.profile_link)))

        login.find_element(By.XPATH, Locator.logo).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.constructor_title)))
        title = login.find_element(By.XPATH, Locator.constructor_title).text
        assert title == "Соберите бургер"

    def test_constructor_to_sauces_navigation(self, login):
        login.find_element(By.XPATH, Locator.sauces).click()
        clicked_sauces = login.find_element(By.XPATH, Locator.active_section).text
        assert clicked_sauces == "Соусы"

    def test_constructor_to_buns_navigation(self, login):
        login.find_element(By.XPATH, Locator.sauces).click()
        login.find_element(By.XPATH, Locator.buns).click()
        clicked_buns = login.find_element(By.XPATH, Locator.buns).text
        assert clicked_buns == "Булки"

    def test_constructor_to_toppings_navigation(self, login):
        login.find_element(By.XPATH, Locator.toppings).click()
        clicked_toppings = login.find_element(By.XPATH, Locator.toppings).text
        assert clicked_toppings == "Начинки"




