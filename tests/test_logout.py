from locator import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestProfileLogout:
    def test_profile_logout(self, login):
        driver = login
        driver.find_element(By.XPATH, Locator.profile_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.logout_button)))
        driver.find_element(By.XPATH, Locator.logout_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.login_title)))
        title = driver.find_element(By.XPATH, Locator.login_title).text
        assert title == "Вход"