# Project Structure

This project is a Playwright E2E Automation Framework implemented using Python and Pytest, following the Page Object Model (POM) design pattern.

## Framework Architecture

The framework is structured to separate test logic from page-specific interactions to ensure maintainability and reusability.

### Directories and Their Purposes

- **`BasePages/`**: Contains the base class definitions for pages. These classes handle generic interactions and shared elements common to multiple pages.
- **`PageObjects/`**: Contains the specific Page Object classes (e.g., `LoginPage`, `DashboardPage`, `GooglePage`). Each class encapsulates the selectors and methods required to interact with a specific page or feature.
- **`data/`**: Stores test data in structured formats (`.json`, `.csv`), allowing tests to be data-driven and separate from the code.
- **`utils/`**: Contains shared utility classes (e.g., `UIUtils.py`) that provide helper methods for common UI actions and assertions across the framework.

- **`test-results/`**: Stores execution outputs, including logs and Playwright trace files for debugging.
- **`assets/`**: Contains static assets like CSS files used for reporting or custom styling.

### Key Files

- **`conftest.py`**: The central Pytest configuration file. It defines shared fixtures (like `browserInstance`, `environment_config`) and manages the test lifecycle.
- **`pytest.ini`**: Configures pytest defaults, such as marker registration (`smoke`, `regression`, `functional`).
- **`test_playwright_e2e_framework.py`**: The main test suite containing end-to-end test cases that orchestrate Page Objects.
- **`test_playwrightBasics.py` & `test_playwright_e2e_python.py`**: Additional test files for basic functionality and standalone scripts.

## Running Tests

Run these commands from the project root using the terminal:

```powershell
pytest -s test_playwright_e2e_framework.py                 # Run all tests in the framework
pytest -s -m smoke test_playwright_e2e_framework.py        # Run only smoke tests
pytest -s -m functional test_playwright_e2e_framework.py  # Run only functional tests
pytest -s --browser firefox test_playwright_e2e_framework.py # Run tests in Firefox
```

### Browser Selection
Use `--browser chromium`, `--browser firefox`, or `--browser webkit` to select a specific browser. If omitted, the framework defaults to Chromium.
