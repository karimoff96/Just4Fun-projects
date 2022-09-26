from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


chrome_driver_path = "Chrome driver direction"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3255772238&f_AL=true&f_E=2%2C3%2C4&geoId=105149562&keywords=python%20developer&location=South%20Korea&refresh=true ")
sign_in = driver.find_element(
    By.PARTIAL_LINK_TEXT, 'Sign in')
sign_in.click()
# time.sleep(3)
phone = driver.find_element(By.ID, 'username')
phone.send_keys('email or phone number')
password = driver.find_element(By.ID, 'password')
password.send_keys('password')
password.send_keys(Keys.ENTER)
time.sleep(5)

all_listings = driver.find_elements_by_css_selector(
    ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(
            ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(
            By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(phone)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME,
                                               "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME,
                                                  "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME,
                                           "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
