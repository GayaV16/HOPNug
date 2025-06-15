import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("file:///C:/Users/Paras/OneDrive/Desktop/demoenvironment.html")
    time.sleep(2)
    yield driver
    driver.close()

@pytest.fixture()
def fill_and_submit_form(driver):
    def fill(vendor: str,amount: str,date: str,status: str):
     vendor_name = driver.find_element(By.ID, "vendor")
     vendor_name.clear()
     vendor_name.send_keys(vendor)
     amount_in = driver.find_element(By.XPATH, "//input[@type='number']")
     amount_in.clear()
     amount_in.send_keys(amount)
     date_in = driver.find_element(By.XPATH, "//input[@name='date']")
     date_in.clear()
     date_in.send_keys(date)
     dropdown = Select(driver.find_element(By.ID, "status"))
     dropdown.select_by_visible_text(status)
     driver.find_element(By.XPATH, "//button[@type='submit']").click()
    return  fill

