import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.positiveflow
def test_validfile_png(driver):
    driver = driver
    driver.find_element(By.ID,"file").send_keys("C:\\Users\\Paras\\Downloads\\Testing\\invoice1.png")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    wait = WebDriverWait (driver,10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID,"success-message")))
    driver.save_screenshot("testcase1.png")
    message = driver.find_element(By.ID,"success-message").text
    print(message)
    assert "successfully" in message

@pytest.mark.positiveflow
def test_validfile_jpg(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\Downloads\\Testing\\invoice2.jpg")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID,"success-message")))
    message = driver.find_element(By.ID,"success-message").text
    print(message)
    driver.save_screenshot('testcase2.png')
    assert "successfully" in message

@pytest.mark.positiveflow
def test_validfile_pdf(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\Downloads\\Testing\\invoice3.pdf")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID,"success-message")))
    message = driver.find_element(By.ID,"success-message").text
    print(message)
    driver.save_screenshot('testcase3.png')
    assert "successfully" in message

@pytest.mark.positiveflow
def test_valid_size(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\Downloads\\Testing\\invoice4.jpeg")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID,"success-message")))
    message = driver.find_element(By.ID,"success-message").text
    print(message)
    driver.save_screenshot('testcase4.png')
    assert "successfully" in message

@pytest.mark.negativeflow
def test_invalidfile_xlxs(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\Downloads\\Testing\\test.xlsx")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, "error-message")))
    message = driver.find_element(By.ID, "error-message").text
    print(message)
    driver.save_screenshot('testcase5.png')
    assert "Only PNG, JPG, or PDF files are allowed." in message

@pytest.mark.negativeflow
def test_invalid_size(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\Downloads\\Testing\\test5.jpg")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, "error-message")))
    message = driver.find_element(By.ID, "error-message").text
    print(message)
    driver.save_screenshot('testcase6.png')
    assert "smaller than 5MB." in message





