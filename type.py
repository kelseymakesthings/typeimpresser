import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait

PATH_TO_CHROMEDRIVER = r'/path/to/your/chromedriver' 
TYPERACER_URL = 'https://play.typeracer.com/'
DELAY_MS = 2
DELAY_POST = 100000

def run():
    ##################### PART 1 #####################
    chrome_driver = webdriver.Chrome()
    # If chromedriver is not in your PATH, change PATH_TO_CHROMEDRIVER and use:
    # chrome_driver = webdriver.Chrome(executable_path=PATH_TO_CHROMEDRIVER)
    chrome_driver.get(TYPERACER_URL)

    ##################### PART 2 #####################
    start_wait = WebDriverWait(chrome_driver, 30)
    start_button = start_wait.until(element_to_be_clickable((By.XPATH, "//a[contains(.,'Enter a typing race')]")))
    start_button.click()

    ##################### PART 3 #####################
    race_text = get_race_text(chrome_driver)

    ##################### PART 4 #####################
    type_wait = WebDriverWait(chrome_driver, 30)
    typing_area = type_wait.until(element_to_be_clickable((By.XPATH, "//input[@class='txtInput']")))
    
    ##################### PART 5 #####################
    for letter in race_text:
        typing_area.send_keys(letter)
        delay = DELAY_MS / 1000
        time.sleep(delay)

    # This is simply to keep the browser open for a while to admire your results
    time.sleep(DELAY_POST)

##################### ALSO PART 3 #####################
def get_race_text(driver):
    wait = WebDriverWait(driver, 30)
    text_elements = wait.until(presence_of_all_elements_located((By.XPATH, "//span[@unselectable='on']")))
    text_parts = [el.text for el in text_elements]
    race_text = ''
    if len(text_parts) == 3:
        race_text = '{}{} {}'.format(text_parts[0], text_parts[1], text_parts[2])
    elif len(text_parts) == 2:
        # One-letter first word
        race_text = '{} {}'.format(text_parts[0], text_parts[1])
    return race_text

if __name__ == '__main__':
    run()
