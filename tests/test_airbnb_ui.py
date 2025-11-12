from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_homepage_loads():
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Open your Flask app homepage
    driver.get("http://localhost:5000")
    
    # Wait briefly for the page to load
    time.sleep(2)
    
    # Verify the title of the page
    assert "Airbnb - Home" in driver.title, "Page title does not match 'Airbnb - Home'"
    
    # Find all hotel cards using the class name
    hotel_cards = driver.find_elements("class name", "hotel-card")
    assert len(hotel_cards) > 0, "No hotel cards found on homepage"
    
    # Print hotel names for verification (optional)
    for card in hotel_cards:
        print(card.text)
    
    # Quit the browser
    driver.quit()
