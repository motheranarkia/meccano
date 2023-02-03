import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dev-cc.mel-meccano.ru/sign-in")
    yield driver
    driver.quit()


def test_login_of_a_registered_user(driver):
    email_field = "//input[@name = 'email']"
    password_field = "//input[@name = 'password']"
    form_submission_button = "//*/button[text() = 'Войти']"

    driver.find_element(By.XPATH, email_field).click()
    driver.find_element(By.XPATH, email_field).send_keys('qa_test@exlibris.ru')
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, password_field)))
    driver.find_element(By.XPATH, password_field).click()
    driver.find_element(By.XPATH, password_field).send_keys('BB20a9or')
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, form_submission_button)))
    driver.find_element(By.XPATH, form_submission_button).click()
    WebDriverWait(driver, 3).until(ec.url_to_be('https://dev-cc.mel-meccano.ru/'))
    assert driver.current_url == 'https://dev-cc.mel-meccano.ru/'
