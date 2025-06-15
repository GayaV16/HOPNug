import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



def test_valid_inputs(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test",amount="50",date="14/06/2025",status="Paid")
    driver.save_screenshot("form_testcase1.png")
    message = driver.find_element(By.ID,"success-box").text
    print(message)
    assert "Form submitted successfully!" in message

def test_invalid_name(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test$%^^", amount="50", date="14/06/2025", status="Paid")
    driver.save_screenshot("form_testcase2.png")
    message = driver.find_element(By.CLASS_NAME, "error").text
    print(message)
    assert "Vendor name must use letters and spaces only." in message

def test_blank_name(driver,fill_and_submit_form):
    fill_and_submit_form(vendor=" ", amount="50", date="14/06/2025", status="Paid")
    driver.save_screenshot("form_testcase3.png")
    message = driver.find_element(By.ID, "vendor-error").text
    print(message)
    assert "Vendor name cannot be empty." in message

def test_negative_amount(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test",amount="-50",date="14/06/2025",status="Paid")
    driver.save_screenshot("form_testcase4.png")
    message = driver.find_element(By.ID,"amount-error").text
    print(message)
    assert "Amount must be a positive number greater than 0." in message

def test_blank_amount(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test", amount=" ", date="15/06/2025", status="Paid")
    driver.save_screenshot("form_testcase5.png")
    message = driver.find_element(By.ID, "amount-error").text
    print(message)
    assert "Amount cannot be empty." in message

def test_valid_pastdate(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test", amount="50", date="14/06/2025", status="Paid")
    driver.save_screenshot("form_testcase6.png")
    message = driver.find_element(By.ID, "success-box").text
    print(message)
    assert "Form submitted successfully!" in message

def test_invalid_futuredate(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test", amount="50", date="16/06/2025", status="Paid")
    driver.save_screenshot("form_testcase7.png")
    message = driver.find_element(By.ID, "date-error").text
    print(message)
    assert "Date cannot be in the future." in message

def test_invalid_dateformat(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test", amount="50", date="01/15/2025", status="Paid")
    driver.save_screenshot("form_testcase8.png")
    message = driver.find_element(By.ID, "date-error").text
    print(message)
    assert "Date must be in dd/mm/yyyy format." in message

def test_blank_date(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test", amount="50", date=" ", status="Paid")
    driver.save_screenshot("form_testcase9.png")
    message = driver.find_element(By.ID, "date-error").text
    print(message)
    assert "Date cannot be empty." in message

def test_valid_status(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test", amount="50", date="14/06/2025", status="Pending")
    driver.save_screenshot("form_testcase10.png")
    message = driver.find_element(By.ID, "success-box").text
    print(message)
    assert "Form submitted successfully!" in message

def test_all_fields_empty(driver,fill_and_submit_form):
    fill_and_submit_form(vendor=" ", amount=" ", date="", status="Paid")
    driver.save_screenshot("form_testcase11.png")
    messages = ["Vendor name cannot be empty.","Amount cannot be empty.","Date cannot be empty."]
    message1 = driver.find_element(By.ID, "vendor-error").text
    message2 = driver.find_element(By.ID, "amount-error").text
    message3 = driver.find_element(By.ID, "date-error").text
    new_messages = [str(message1),str(message2),str(message3)]
    print(new_messages)
    assert messages == new_messages

def test_invalid_name_sql_injection(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="admin' -- ", amount="50", date="14/06/2025", status="Paid")
    driver.save_screenshot("form_testcase12.png")
    message = driver.find_element(By.CLASS_NAME, "error").text
    print(message)
    assert "Vendor name must use letters and spaces only." in message

def test_nonnumeric_amount(driver,fill_and_submit_form):
    fill_and_submit_form(vendor="Test",amount="50agbjh",date="14/06/2025",status="Paid")
    driver.save_screenshot("form_testcase13.png")
    message = driver.find_element(By.ID,"amount-error").text
    print(message)
    assert "Amount must be a positive number greater than 0." in message


