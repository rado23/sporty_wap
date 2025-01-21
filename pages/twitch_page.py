from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TwitchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements to appear

    def open(self):
        self.driver.get("https://m.twitch.tv/")
        time.sleep(2)  # Wait for elements to appear
        self.accept_consent_banner()

    def accept_consent_banner(self):
        try:
            print("🔍 Checking for consent banner...")
            consent_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-a-target='consent-banner-accept']")
            consent_button.click()
            print("✅ Consent banner accepted.")
        except:
            print("❌ No consent banner found.")

    def open_browse_page(self):
        try:
            print("🔍 Opening Browse page...")
            browse_page_button = self.driver.find_element(By.CSS_SELECTOR, "a[href='/directory']")
            browse_page_button.click()
            print("✅ Browse page opened.")
        except:
            print("❌ No Browse button found.")

    def click_search_field(self):
        try:
            print("🔍 Waiting for the search field to become clickable...")
            search_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='search']")))
            print("✅ Search input field found, clicking it...")
            search_input.click()
        except Exception as e:
            print(f"❌ Could not find the search input field: {e}")
            raise

    def search_game(self, game_name):
        search_box = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']")))
        search_box.send_keys(game_name)
        search_box.send_keys(Keys.RETURN)

    def scroll_down(self, count):
        for _ in range(count):
            self.driver.execute_script("window.scrollBy(0, 500)")
            self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            time.sleep(1)

    def select_streamer(self):
        print("🔍 Looking for 'VIDEOS' section...")
        videos_section = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'VIDEOS')]")))

        print("✅ Found 'VIDEOS' section, selecting a streamer with an image and views...")
        streamer = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                   "//h2[contains(text(), 'VIDEOS')]/following::div//a[contains(@class, 'tw-link')][descendant::span[contains(@title, 'views')]]")))

        if streamer.is_displayed():
            print("✅ Clicking on the visible streamer with an image and views...")
            streamer.click()
        else:
            raise Exception("❌ No visible streamers with images and views found after scrolling.")

    def handle_modals_and_screenshot(self):
        time.sleep(5)
        modal_close_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Close']")
        for btn in modal_close_buttons:
            btn.click()
        self.driver.save_screenshot("screenshot.png")
        print("📸 Screenshot taken: screenshot.png")