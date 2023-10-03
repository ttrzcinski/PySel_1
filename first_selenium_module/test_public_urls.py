from selenium import webdriver


def test_google_pl():
    # Arrange
    # Get the driver
    driver = webdriver.Chrome()
    # Maximize that Chrome
    driver.maximize_window()

    # Act
    # Get url response
    driver.get("https://www.google.pl/")

    # Assert
    # Check title
    assert(driver.title is not None)
