import webbrowser
import time
import pyautogui

def open_and_refresh_browser(url, num_windows, refresh_interval):
    """
    Opens multiple browser windows to the same URL and refreshes them after a specified interval.

    Args:
        url (str): The URL to open.
        num_windows (int): Number of browser windows to open.
        refresh_interval (int): Time interval in seconds to refresh the windows.
    """
    # Open the specified number of browser windows
    for _ in range(num_windows):
        webbrowser.open(url)
        time.sleep(1)  # Slight delay to prevent system overload
    
    print(f"Opened {num_windows} windows with URL: {url}")
    print(f"Refreshing every {refresh_interval} seconds...")
    
    try:
        while True:
            time.sleep(refresh_interval)
            pyautogui.hotkey("ctrl", "r")  # Simulate refresh (Ctrl+R)
            print("Refreshed all open browser tabs.")
    except KeyboardInterrupt:
        print("Stopped refreshing browser windows.")

# Customize parameters
url_to_open = "https://www.youtube.com"  # Replace with your desired URL
number_of_windows = 4  # Number of windows to open
refresh_time = 30  # Refresh interval in seconds

open_and_refresh_browser(url_to_open, number_of_windows, refresh_time)
