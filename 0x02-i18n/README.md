# 0x02. i18n

This project is part of the ALX Software Engineering program, focusing on implementing internationalization (i18n) in a Flask application. It introduces key concepts in localization, language support, and timezone management.

## Table of Contents

- [Introduction](#introduction)
- [Concepts and Skills](#concepts-and-skills)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Author](#author)

---

## Introduction

In this project, you will learn how to implement internationalization (i18n) in a Flask application. This project explores how to support multiple languages and manage timezones in a web application.

### Objectives

- Understand the internationalization process.
- Implement language support in Flask.
- Learn about timezone management.

**Key Topics Covered:**

- Internationalization (i18n)
- Localization (l10n)
- Flask framework
- Babel library

---

## Concepts and Skills

### Key Topics

1. **Internationalization (i18n)**:
   - What internationalization means.
   - Implementing language support in a Flask application.

2. **Localization (l10n)**:
   - How to localize content based on user preferences.
   - Managing translations and language files.

3. **Timezone Management**:
   - Understanding timezones and their importance.
   - Handling timezones in a web application.

4. **Python Programming**:
   - Writing secure and efficient code.
   - Adhering to the **PEP 8 style guide**.

---

## Requirements

### General

- **Allowed editors**: `vi`, `vim`, `emacs`.
- Code will be interpreted/compiled on **Ubuntu 18.04 LTS** using Python 3.7.
- Adhere to the **PEP 8 style guide** (version 2.5).
- No external module imports unless specified.
- All files should:
  - End with a new line.
  - Be executable.
  - Include proper documentation for modules, classes, and functions.

### Repository Structure

- **GitHub repository**: [alx-backend](https://github.com/Tariq5mo/alx-backend)
- **Directory**: `0x02-i18n`
- **Files**:
  - `0-app.py`: Basic Flask app setup.
  - `1-app.py`: Basic Babel setup.
  - `2-app.py`: Get locale from request.
  - `3-app.py`: Parametrize templates.
  - `4-app.py`: Force locale with URL parameter.
  - `5-app.py`: Mock logging in.
  - `6-app.py`: Use user locale.
  - `7-app.py`: Infer appropriate time zone.
  - `8-app.py`: Display the current time.

---

## Project Tasks

### **0. Basic Flask app**

Set up a basic Flask app with a single `/` route and an `index.html` template that outputs "Welcome to ALX" as the page title and "Hello world" as the header.

### **1. Basic Babel setup**

Install the Babel Flask extension and configure available languages in the app.

### **2. Get locale from request**

Create a `get_locale` function to determine the best match with supported languages.

### **3. Parametrize templates**

Use the `_` or `gettext` function to parametrize templates and manage translations.

### **4. Force locale with URL parameter**

Implement a way to force a particular locale by passing the `locale` parameter in the URL.

### **5. Mock logging in**

Mock a user login system and display a welcome message based on the logged-in user.

### **6. Use user locale**

Change the `get_locale` function to use a user's preferred locale if supported.

### **7. Infer appropriate time zone**

Define a `get_timezone` function to infer the appropriate time zone based on URL parameters or user settings.

### **8. Display the current time**

Display the current time on the home page based on the inferred time zone.

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Tariq5mo/alx-backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x02-i18n
   ```

3. Install the dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   FLASK_APP=0-app.py flask run
   ```

---

## Author

This project was completed by **Tariq Omer**, a student of the ALX Software Engineering program specializing in back-end development. Connect with me on [GitHub](https://github.com/Tariq5mo).
