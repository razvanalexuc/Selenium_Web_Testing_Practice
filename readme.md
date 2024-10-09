# Selenium_Web_Testing_Practice

This repository contains automated web testing scripts created using Python's Selenium WebDriver. It covers various scenarios such as form field input, table interactions, dynamic elements, and login functionality on different websites. The scripts aim to provide hands-on practice with web automation techniques using the Page Object Model (POM).

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Test Cases](#test-cases)
  - [TestAutomation Practice Blog](#testautomation-practice-blog)
  - [USV Moodle Login](#usv-moodle-login)
  - [PracticeTestAutomation Login](#practicetestautomation-login)
- [Execution](#execution)
- [References](#references)

## Overview
This project demonstrates various web testing scenarios automated with Selenium. The following operations are included:
- Form submission
- Table interaction
- Handling dynamic elements (buttons, alerts)
- Drag and drop, slider movements
- Positive and negative login tests

The repository showcases test scripts built for different websites, with an emphasis on applying the Page Object Model (POM) pattern for better code structure and maintainability.

## Prerequisites
- Python 3.x
- Selenium
- Chrome WebDriver Manager
- Google Chrome Browser

## Setup

1. Clone the repository:
```bash
git clone https://github.com/razvanalexuc/Selenium_Web_Testing_Practice.git
```
2. Navigate to the project directory:
```bash
cd Selenium_Web_Testing_Practice
```
  
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Test Cases

### TestAutomation Practice Blog
The script in `testpractice_blogspot.py` interacts with a demo site hosted at [TestAutomationPractice](https://testautomationpractice.blogspot.com):
- Filling out form fields (name, email, phone, address)
- Handling cookie banners
- Table interaction (HTML and pagination-based)
- Dynamic button interaction
- Handling alerts and prompt boxes
- Drag and drop elements and moving sliders

For a detailed example of these interactions, refer to the file `testpractice_blogspot.py`.

### USV Moodle Login
In `usv_page_object.py`, the script tests the login functionality for the USV Moodle site:
- Entering username and password
- Handling login actions
- Basic Page Object Model for login

For more details, see the file `usv_page_object.py`.

### PracticeTestAutomation Login
The script in `testautomation_page_object.py` handles login scenarios at [PracticeTestAutomation](https://practicetestautomation.com/practice-test-login/). It contains:
- Positive test case: Valid login credentials
- Negative test cases: Invalid username and invalid password
- Assertion of error messages
  
For more details, refer to `testautomation_page_object.py`.

### Execution
To run the tests, execute the individual test files using Python:

  ```bash
  python testpractice_blogspot.py
  python usv_page_object.py
  python testautomation_page_object.py
```
## References
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/)
- [TestAutomationPractice](https://testautomationpractice.blogspot.com)
- [PracticeTestAutomation](https://practicetestautomation.com)
