# Selenium 3 to Selenium 4 Code Upgrade Script

This project contains a Python script that automatically upgrades Selenium 3 code to Selenium 4. The script reads Selenium 3 code from a text file, converts it to Selenium 4 syntax, and saves the upgraded code to a new file.

## Features

- Converts `find_element_by_*` methods to the new Selenium 4 `find_element(By.*)` syntax.
- Automatically adds necessary imports for Selenium 4.
- Saves the upgraded code to an output file.

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the script file.
2. Ensure you have Python 3.x installed on your machine.

## Usage

1. Create a text file named `input.txt` in the same directory as the script. Place your Selenium 3 code in this file. Here is an example of what your `input.txt` might look like:

   ```python
   driver.find_element_by_id("emailAddress").send_keys(Keys.ENTER)
   driver.find_element_by_xpath("//main[@id='skip-target']/div/div").click()
   driver.find_element_by_xpath("//summary[@id='check-email']/span").click()
   ```

2. Run the script:

   ```bash
   python upgrade_selenium.py
   ```

3. After running the script, a new file named `output.txt` will be created in the same directory. This file contains your upgraded Selenium 4 code.

## Example Output

For the above `input.txt`, the `output.txt` will look like this:

```python
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "emailAddress").send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "//main[@id='skip-target']/div/div").click()
driver.find_element(By.XPATH, "//summary[@id='check-email']/span").click()
```
