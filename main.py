import os
import re

def upgrade_selenium_code(input_filename, output_filename):
    # Check if the input file exists
    if not os.path.exists(input_filename):
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    
    # Define a mapping from Selenium 3 to Selenium 4 methods
    selenium_3_to_4_map = {
        'find_element_by_id': 'find_element(By.ID, {})',
        'find_element_by_xpath': 'find_element(By.XPATH, {})',
        'find_element_by_name': 'find_element(By.NAME, {})',
        'find_element_by_class_name': 'find_element(By.CLASS_NAME, {})',
        'find_element_by_tag_name': 'find_element(By.TAG_NAME, {})',
        'find_element_by_link_text': 'find_element(By.LINK_TEXT, {})',
        'find_element_by_partial_link_text': 'find_element(By.PARTIAL_LINK_TEXT, {})',
    }

    # Read the input file
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()

    # Open the output file for writing
    with open(output_filename, 'w') as output_file:
        # Write the necessary imports for Selenium 4
        output_file.write('from selenium.webdriver.common.by import By\n\n')

        # Regular expression pattern to match the old method syntax
        pattern = re.compile(r'(\w+)\((["\'])(.+?)(["\'])\)')

        # Process each line and replace Selenium 3 methods with Selenium 4 methods
        for line in lines:
            # Trim whitespace from the line
            stripped_line = line.strip()

            # Search for the pattern in the line
            match = pattern.search(stripped_line)
            if match:
                # Extract the method, quote, and argument from the matched groups
                old_method = match.group(1)
                quote = match.group(2)
                argument = match.group(3)

                # Replace old method with the new method format
                if old_method in selenium_3_to_4_map:
                    new_method = selenium_3_to_4_map[old_method].format(f'{quote}{argument}{quote}')
                    updated_line = stripped_line.replace(
                        f'{old_method}({quote}{argument}{quote})',
                        new_method
                    )
                    output_file.write(updated_line + '\n')
                else:
                    output_file.write(line)
            else:
                # If no replacements are made, write the original line
                output_file.write(line)

    print(f"Upgrade complete! The upgraded code has been saved to '{output_filename}'.")

# File names
input_file_name = 'input.txt'
output_file_name = 'output.txt'

# Run the upgrade function
upgrade_selenium_code(input_file_name, output_file_name)
