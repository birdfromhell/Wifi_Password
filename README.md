# Windows-WiFi-Extractor
Extract Windows Wi-Fi Passwords to a Remote URL

# Install
Before running, install the required modules:

```
pip3 install -r requirements.txt
```

# Usage
To use, simply replace the `url` variable with your webhook and execute the following:

```
python main.py
```

# Making an executable
If you want to be a fancy pants, you can convert this to an exe :)

```
#install pyinstaller 
pip install pyinstaller


pyinstaller --onefile main.py
```