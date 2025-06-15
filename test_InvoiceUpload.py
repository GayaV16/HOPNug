import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.positiveflow
def test_validfile_png(driver):
    driver = driver
    driver.find_element(By.ID,"file").send_keys("C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Datafile\\invoice1.png")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    wait = WebDriverWait (driver,10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID,"success-message")))
    path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Invoice_testcases_screenshots\\testcase1.png"
    driver.save_screenshot(path)
    message = driver.find_element(By.ID,"success-message").text
    print(message)
    assert "successfully" in message

@pytest.mark.positiveflow
def test_validfile_jpg(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Datafile\\invoice2.jpg")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID,"success-message")))
    message = driver.find_element(By.ID,"success-message").text
    print(message)
    path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Invoice_testcases_screenshots\\testcase2.png"
    driver.save_screenshot(path)
    assert "successfully" in message

@pytest.mark.positiveflow
def test_validfile_pdf(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Datafile\\invoice3.pdf")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID,"success-message")))
    message = driver.find_element(By.ID,"success-message").text
    print(message)
    path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Invoice_testcases_screenshots\\testcase3.png"
    driver.save_screenshot(path)
    assert "successfully" in message

@pytest.mark.positiveflow
def test_valid_size(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Datafile\\invoice4.jpeg")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID,"success-message")))
    message = driver.find_element(By.ID,"success-message").text
    print(message)
    path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Invoice_testcases_screenshots\\testcase4.png"
    driver.save_screenshot(path)
    assert "successfully" in message

@pytest.mark.negativeflow
def test_invalidfile_xlxs(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Datafile\\test.xlsx")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, "error-message")))
    message = driver.find_element(By.ID, "error-message").text
    print(message)
    path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Invoice_testcases_screenshots\\testcase5.png"
    driver.save_screenshot(path)
    assert "Only PNG, JPG, or PDF files are allowed." in message

@pytest.mark.negativeflow
def test_invalid_size(driver):
    driver = driver
    driver.find_element(By.ID, "file").send_keys("C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Datafile\\test5.jpg")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, "error-message")))
    message = driver.find_element(By.ID, "error-message").text
    print(message)
    path = "C:\\Users\\Paras\\PycharmProjects\\pythonProject\\HOPN ug\\Invoice_testcases_screenshots\\testcase6.png"
    driver.save_screenshot(path)
    assert "smaller than 5MB." in message





