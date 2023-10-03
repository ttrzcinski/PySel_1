from selenium import webdriver


def test_google_pl():
    # Get the driver
    driver = webdriver.Chrome()
    # Maximize that Chrome
    driver.maximize_window()
    # Get url response
    driver.get("https://www.google.pl/")
    # Check title
    print("The tile is: ", driver.title)
