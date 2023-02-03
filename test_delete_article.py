import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dev-cc.mel-meccano.ru/sign-in")
    yield driver
    driver.quit()


def test_remove_article(driver):
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

    driver.get("https://dev-cc.mel-meccano.ru/innopolis/messages?message-type=smi&property=all")

    article = driver.find_element(
        By.XPATH,
        "//h3[text()='AgroCode Awards 2022: Россельхозбанк наградил самые успешные агротех-стартапы']"
    )

    delete_button = driver.find_element(
        By.XPATH,
        "//*[@id='root']/div/div[1]/main/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[3]/div[3]/div/button"
    )
    delete_button.click()

    confirm_delete = driver.find_element(By.XPATH, "//*/button[text() = 'Применить']")
    confirm_delete.click()

    WebDriverWait(driver, 10).until(ec.staleness_of(article))

    with pytest.raises(NoSuchElementException):
        driver.find_element(
            By.XPATH,
            "//h3[text()='AgroCode Awards 2022: Россельхозбанк наградил самые успешные агротех-стартапы']"
        )
