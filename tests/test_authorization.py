from locator import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestAuthorization:
    def test_authorization_by_login_button_on_main_page(self, driver):
        driver.find_element(By.XPATH, Locator.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_email)))

        driver.find_element(By.XPATH, Locator.authorization_email).send_keys('anna_krylova_8_123@yandex.ru')
        driver.find_element(By.XPATH, Locator.authorization_password).send_keys('randompass123')
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_button)))
        driver.find_element(By.XPATH, Locator.authorization_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.constructor_title)))

        title = driver.find_element(By.XPATH, Locator.constructor_title).text
        assert title == "Соберите бургер"
        #print(title)

    def test_authorization_from_profile_page(self, driver):
        driver.find_element(By.XPATH, Locator.profile_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_email)))

        driver.find_element(By.XPATH, Locator.authorization_email).send_keys('anna_krylova_8_123@yandex.ru')
        driver.find_element(By.XPATH, Locator.authorization_password).send_keys('randompass123')
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_button)))
        driver.find_element(By.XPATH, Locator.authorization_button).click()

    def test_authorization_from_registration_form(self, driver):
        driver.find_element(By.XPATH, Locator.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_email)))
        driver.find_element(By.XPATH, Locator.registration_link).click()
        driver.find_element(By.XPATH, Locator.login_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.login_title)))

        #text = driver.find_element(By.XPATH, Locator.login_title).text
        #assert text == "Вход"

        driver.find_element(By.XPATH, Locator.authorization_email).send_keys('anna_krylova_8_123@yandex.ru')
        driver.find_element(By.XPATH, Locator.authorization_password).send_keys('randompass123')
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_button)))
        driver.find_element(By.XPATH, Locator.authorization_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.constructor_title)))

        title = driver.find_element(By.XPATH, Locator.constructor_title).text
        assert title == "Соберите бургер"

    def test_authorization_from_pass_restoration_form(self, driver):
        driver.find_element(By.XPATH, Locator.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_email)))
        driver.find_element(By.XPATH, Locator.pass_restoration_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.pass_restoration_title)))
        driver.find_element(By.XPATH, Locator.login_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_email)))

        driver.find_element(By.XPATH, Locator.authorization_email).send_keys('anna_krylova_8_123@yandex.ru')
        driver.find_element(By.XPATH, Locator.authorization_password).send_keys('randompass123')
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.authorization_button)))
        driver.find_element(By.XPATH, Locator.authorization_button).click()


