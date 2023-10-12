# Wi-Fi Password Extractor

The Wi-Fi Password Extractor is a Python based application which retrieves saved Wi-Fi passwords from a system and sends them to a specific webhook URL.

## Description

This application uses Tkinter to provide a graphical user interface where users can input their webhook URL then trigger the password extraction process by clicking a button. This application further utilizes the built-in 'netsh' command available on Windows systems to retrieve the SSID and associated passwords of all remembered Wi-Fi networks.

## Dependencies

The application requires the following Python libraries:
* tkinter
* re
* requests
* subprocess
* sys

To install the dependencies, use:
Usage
* Run the application.
* Enter your webhook URL in the input box.
* Click the 'Start' button to start the process.

The application will retrieve remembered Wi-Fi SSIDs and their corresponding passwords and send them to the provided webhook URL.
Note: Do NOT use this application for any malicious intent. This is intended for legitimately retrieving forgotten passwords and for educational purposes only.