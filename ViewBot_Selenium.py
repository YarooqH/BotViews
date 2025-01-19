from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager

import time

def open_and_refresh_browser(url, num_windows, refresh_interval, open_as_tabs=True):
    """
    Opens multiple browser instances or tabs to the same URL and refreshes them after a specified interval.

    Args:
        url (str): The URL to open.
        num_windows (int): Number of browser instances or tabs to open.
        refresh_interval (int): Time interval in seconds to refresh the pages.
        open_as_tabs (bool): Whether to open the URLs as tabs (True) or separate windows (False).
    """
    # Set up the WebDriver for Chrome
    service = Service(ChromeDriverManager().install())  # Add the path to chromedriver if it's not in your PATH
    # options = webdriver.ChromeOptions()
    print("Just Checking")
    driver = webdriver.Chrome(service = service)
    print("-- Created Driver --")
    # driver = webdriver.Chrome(service=service, options=options)

    # Open the first instance (main window or tab)
    driver.get(url)
    print(f"Opened: {url}")

    # Open additional tabs or windows
    for i in range(1, num_windows):
        if open_as_tabs:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
        else:
            # options = webdriver.ChromeOptions()
            # driver_new = webdriver.Chrome(service=service, options=options)
            driver_new =  webdriver.Chrome(service = service)
            driver_new.get(url)
            print(f"Opened new window for: {url}")
            continue
        
        driver.get(url)
        print(f"Opened tab {i + 1}: {url}")

    print(f"Opened {num_windows} {'tabs' if open_as_tabs else 'windows'} with URL: {url}")
    print(f"Refreshing every {refresh_interval} seconds...")

    # Continuous refresh
    try:
        while True:
            time.sleep(refresh_interval)
            if open_as_tabs:
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    driver.refresh()
            else:
                # Refresh each window (only relevant if `open_as_tabs` is False)
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    driver.refresh()
            
            print("Refreshed all pages.")
    except KeyboardInterrupt:
        print("Stopped refreshing browser pages.")
        driver.quit()

# Customize parameters
url_to_open = "https://www.youtube.com"  # Replace with your desired URL
number_of_windows = 3  # Number of tabs/windows to open
refresh_time = 20  # Refresh interval in seconds
open_as_tabs = True  # True for tabs, False for separate windows

open_and_refresh_browser(url_to_open, number_of_windows, refresh_time, open_as_tabs)
