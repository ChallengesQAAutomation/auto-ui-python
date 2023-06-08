# Selenium Automation Script

This script is designed to automate web testing using Selenium WebDriver with Chrome and Firefox browsers. It allows you to run automated tests on macOS, leveraging the available drivers for Chrome and Firefox.

## Prerequisites

- Python 3.7 or higher installed
- Selenium WebDriver for Python installed (`pip install selenium`)
- ChromeDriver for Chrome browser: Download the appropriate version for your operating system [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- GeckoDriver for Firefox browser: Download the appropriate version for your operating system [here](https://github.com/mozilla/geckodriver/releases)

## Instructions ** Find broken links **
1. Clone the repository or download the script to your local machine.
2. Place the downloaded ChromeDriver and GeckoDriver executables in the same directory as the script.
3. Open the script in a text editor and modify the `url` variable with your desired URL to test.
4. Run the script using `python broken_links_script`.

## Usage
The script will open the specified URL in both Chrome and Firefox browsers, perform automated actions, and validate the results. You can customize the test steps and assertions according to your specific requirements.

Please note that the ChromeDriver and GeckoDriver provided are for macOS. For Windows, download the corresponding drivers from the links provided in the Prerequisites section.

For any issues or questions, feel free to reach out.

Happy testing!
