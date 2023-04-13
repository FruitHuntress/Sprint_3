from faker import Faker
from locator import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

faker = Faker()

class TestRegistration:
    def test_registration_with_all_correct_fields(self, driver):
        email = faker.email()

        driver.find_element(By.XPATH, Locator.login_button).click()
        driver.find_element(By.XPATH, Locator.registration_link).click()

        driver.find_element(By.NAME, Locator.name).send_keys("Ann")
        driver.find_element(By.XPATH, Locator.registration_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.registration_password).send_keys("randompass123")

        driver.find_element(By.XPATH, Locator.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.login_title)))
        title = driver.find_element(By.XPATH, Locator.login_title).text
        assert title == "Вход"



    def test_registration_with_empty_name(self, driver):
        email = faker.email()

        driver.find_element(By.XPATH, Locator.login_button).click()
        driver.find_element(By.XPATH, Locator.registration_link).click()

        driver.find_element(By.XPATH, Locator.registration_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.registration_password).send_keys("randompass123")

        driver.find_element(By.XPATH, Locator.registration_button).click()
        button_text = driver.find_element(By.XPATH, Locator.registration_button).text
        assert button_text == "Зарегистрироваться"

    def test_registration_with_wrong_pass(self, driver):
        email = faker.email()

        driver.find_element(By.XPATH, Locator.login_button).click()
        driver.find_element(By.XPATH, Locator.registration_link).click()

        driver.find_element(By.XPATH, Locator.registration_email).send_keys(email)
        driver.find_element(By.XPATH, Locator.registration_password).send_keys("123")

        driver.find_element(By.XPATH, Locator.registration_button).click()
        text = driver.find_element(By.XPATH, Locator.incorrect_pass).text
        assert text == "Некорректный пароль"