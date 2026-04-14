# Urban Routes - Selenium QA Automation

## Project Overview
This project automates end-to-end tests for the Urban Routes web application, a ride-booking platform where users enter pickup and destination locations, choose a ride plan, add payment details, and place an order.

The automation is written with Python, Selenium, and Pytest using the Page Object Model pattern.

---

## Automated Scenarios

- Set pickup and destination addresses
- Select the Supportive ride plan
- Add and confirm a phone number
- Add a payment card
- Add a comment for the driver
- Order blanket and handkerchiefs
- Order two ice creams
- Verify the car search modal appears

---

## Project Structure

- `test_urban_routes.py` - Pytest test cases
- `pages.py` - Page Object Model methods and locators
- `data.py` - Test data and application URL
- `helpers.py` - Utility functions for URL checks and SMS code retrieval
- `requirements.txt` - Python dependencies

---

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the tests:

```bash
pytest
```

To use a different Urban Routes environment, set the `URBAN_ROUTES_URL` environment variable before running the tests.

---

## Tools Used

- Python
- Selenium WebDriver
- Pytest
- Chrome DevTools
- Git and GitHub

---

## QA Notes

The tests use explicit waits through the page object instead of fixed sleeps. This makes the suite more stable because each action waits for the element state it needs, such as visibility or clickability.

The phone confirmation helper reads Chrome performance logs, so Chrome is started with performance logging enabled in the test setup.
