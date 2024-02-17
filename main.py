import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN_URL = "https://indian-vaccine.web.app/"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#verify the covid cases are accurately loaded according to the selected district
def test_covid_cases(driver):

    #to_launch_url
    driver.get(LOGIN_URL)
    time.sleep(3)

    #to_take_covid_cases_page
    covid_cases_link = driver.find_element(By.XPATH, "//a[normalize-space()='Covid Cases']")
    covid_cases_link.click()
    time.sleep(3)

    #verification_of_title
    covid_cases_element = driver.find_element(By.XPATH, "//h5[normalize-space()='Covid Cases']")
    actual_text = covid_cases_element.text
    expected_text = "Covid Cases"
    assert actual_text == expected_text, f"Expected text '{expected_text}' but found '{actual_text}'"
    time.sleep(3)

    #to_select_a_district
    select_district = driver.find_element(By.XPATH, "//select[@name='selectedDistrict']")
    select_district.click()
    district = driver.find_element(By.XPATH, "//option[normalize-space()='Thiruvananthapuram']")
    district.click()
    time.sleep(3)

    #verification_of_selected_district
    selected_district_element = driver.find_element(By.XPATH, "//h4[normalize-space()='District - Thiruvananthapuram']")
    selected_district_element.click()
    actual_text = selected_district_element.text
    expected_text = "District - Thiruvananthapuram"
    assert actual_text == expected_text, f"Expected text '{expected_text}' but found '{actual_text}'"
    time.sleep(3)


