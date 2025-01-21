import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
try:
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    ChromeDriverManager = None


def get_mobile_driver():
    mobile_emulation = {"deviceName": "Pixel 2"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    print(f"🚀 Initializing WebDriver...")

    if ChromeDriverManager:
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            print("✅ WebDriver initialized successfully.")
        except Exception as e:
            print(f"❌ WebDriver initialization failed: {e}")
            raise
    else:
        try:
            driver = webdriver.Chrome(options=options)
            print("✅ WebDriver initialized successfully (without ChromeDriverManager).")
        except Exception as e:
            print(f"❌ WebDriver initialization failed: {e}")
            raise

    return driver


@pytest.fixture
def driver():
    print(f"🚀 Running WebDriver fixture!")
    driver = get_mobile_driver()
    print("✅ WebDriver started successfully!")
    yield driver
    driver.quit()
    print("🛑 WebDriver closed!")
