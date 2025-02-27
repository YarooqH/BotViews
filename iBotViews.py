import webbrowser
import time
import pyautogui
import psutil
import tkinter as tk
from threading import Thread
from tkinter import messagebox

class BrowserAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("iBotViews")

        # UI Components
        tk.Label(root, text="URL:").grid(row=0, column=0, padx=5, pady=5)
        self.url_entry = tk.Entry(root, width=40)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)
        self.url_entry.insert(0, "https://www.youtube.com")

        tk.Label(root, text="Number of Windows:").grid(row=1, column=0, padx=5, pady=5)
        self.num_windows_entry = tk.Entry(root, width=10)
        self.num_windows_entry.grid(row=1, column=1, padx=5, pady=5)
        self.num_windows_entry.insert(0, "4")

        tk.Label(root, text="Refresh Interval (s):").grid(row=2, column=0, padx=5, pady=5)
        self.refresh_interval_entry = tk.Entry(root, width=10)
        self.refresh_interval_entry.grid(row=2, column=1, padx=5, pady=5)
        self.refresh_interval_entry.insert(0, "30")

        self.start_button = tk.Button(root, text="Start", command=self.start_browser)
        self.start_button.grid(row=3, column=0, padx=5, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_browser, state=tk.DISABLED)
        self.stop_button.grid(row=3, column=1, padx=5, pady=10)

        self.running = False
        self.opened_processes = []

    def open_and_refresh(self, url, num_windows, refresh_interval):
        """ Opens multiple browser windows and refreshes them periodically. """
        self.running = True
        for _ in range(num_windows):
            process = webbrowser.open(url)
            time.sleep(1)  # Delay to prevent overload

        messagebox.showinfo("Info", f"Opened {num_windows} windows with URL: {url}")

        while self.running:
            time.sleep(refresh_interval)
            pyautogui.hotkey("ctrl", "r")  # Simulate refresh (Ctrl+R)
            print("Refreshed all open browser tabs.")

    def start_browser(self):
        """ Starts the browser automation in a separate thread. """
        try:
            url = self.url_entry.get()
            num_windows = int(self.num_windows_entry.get())
            refresh_interval = int(self.refresh_interval_entry.get())

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

            # Run in a separate thread to avoid freezing the UI
            self.thread = Thread(target=self.open_and_refresh, args=(url, num_windows, refresh_interval))
            self.thread.daemon = True
            self.thread.start()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for number of windows and refresh interval.")

    def stop_browser(self):
        """ Stops refreshing and closes all opened browser windows. """
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        # Close all browser instances
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if "chrome" in proc.info['name'].lower() or "firefox" in proc.info['name'].lower() or "safari" in proc.info['name'].lower():
                try:
                    proc.terminate()
                except psutil.NoSuchProcess:
                    pass

        messagebox.showinfo("Info", "Stopped all browser windows.")

# Run the GUI
root = tk.Tk()
app = BrowserAutomationApp(root)
root.mainloop()
