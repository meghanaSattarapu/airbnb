from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_wordle_page_loads():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:5000")

    # Check title
    assert "Wordle" in driver.title or "Mini Wordle" in driver.title

    # Check board exists (6 rows, 5 tiles)
    rows = driver.find_elements(By.CLASS_NAME, "row")
    assert len(rows) == 6

    tiles = driver.find_elements(By.CLASS_NAME, "tile")
    assert len(tiles) == 30   # 6 × 5

    # Check keyboard exists
    keys = driver.find_elements(By.CLASS_NAME, "key")
    assert len(keys) > 20     # Full keyboard including enter/backspace

    # Type a sample word: 'apple'
    for letter in "apple":
        key_btn = driver.find_element(By.CSS_SELECTOR, f"button[data-key='{letter}']")
        key_btn.click()
        time.sleep(0.1)

    # Press Enter
    enter_key = driver.find_element(By.CSS_SELECTOR, "button[data-key='enter']")
    enter_key.click()
    time.sleep(1)

    # Now press Backspace to test delete
    back_key = driver.find_element(By.CSS_SELECTOR, "button[data-key='back']")
    back_key.click()
    time.sleep(0.3)

    # Final assertion: page did not crash
    assert "Mini Wordle" in driver.page_source

    driver.quit()
