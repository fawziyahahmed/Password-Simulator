# Random Password Generator
#### The Random Password Generator is a Python script that generates random passwords of specified lengths and checks if they meet certain criteria for acceptability. This tool can be used to create strong and secure passwords for various purposes, such as user authentication or data encryption.
##
## Features
### Random Password Generation: 
#### The script generates random passwords using a combination of uppercase letters, lowercase letters, digits, and special characters.
### Password Acceptability Check: 
#### After generating each password, the script checks if it meets certain criteria for acceptability, such as containing special symbols and not being a common word.
### Customizable Parameters: 
#### Users can customize the length of the generated passwords and adjust the criteria for password acceptability as needed.
##
## How to Use
#### 1. Running the Script: Execute the Python script containing the password generator functions.
#### 2. Password Generation: The script will generate random passwords and display them along with their acceptance status.
#### 3. Acceptance Criteria: By default, passwords must contain special symbols and not be common words (e.g., "password", "123456"). Users can adjust the acceptance criteria by modifying the is_acceptable function.
#### 4. Output: Accepted passwords are stored in a list and displayed at the end of the script execution.
##
## Customization
### Password Length: 
#### Adjust the length of the generated passwords by modifying the length parameter in the generate_password function.
### Acceptance Criteria: 
#### Modify the is_acceptable function to customize the criteria for password acceptability. For example, you can add or remove conditions based on your specific requirements.
##
## Requirements
#### Python 3
