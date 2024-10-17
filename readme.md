# Download and install Pycharm Community Edition

https://www.jetbrains.com/pycharm/download/other.html

# Download and install Allure for windows

https://allurereport.org/docs/install-for-windows/#install-from-an-archive

# Install the pytest-playwright package.

pip install pytest-playwright

# Install the necessary browser binaries for Playwright.

playwright install

# Install the Behave BDD framework.

pip install behave

# Install the PyYAML package.

pip install PyYAML

# Install the Allure adapter for Behave.

pip install allure-behave

# Execute Behave tests with a specified environment.

behave -D ENV=staging headless=false
or
behave -D ENV=staging headless=true

# Generate a single-file Allure test report.

allure generate --single-file --clean --name "Euronics Test Report"

# Open the Allure test report.

allure open
