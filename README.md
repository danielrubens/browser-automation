## Web Scraping Bots, Browser Automation and Testing

 This a python ETL project running on Chrome Web Driver. First, install the libraries:

```bash
pip install requirements.txt
```
To ensure your Google Chrome version, go to the browser and type:
```bash
chrome://version/
```

This will be the equivalent version that you will download at [ChromeDriverStorage](https://chromedriver.storage.googleapis.com/index.html) and extract to the SeleniumDrivers folder.
In booking/constants.py to the SELENIUM_DRIVER variable will be assigned the relative path to the ChromeDriver (that is in the SeleniumDrivers folder)

Then, run in your root directory the following command: 
```bash
python3 run.py
```