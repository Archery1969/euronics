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

behave -D ENV=stg

# Generate a single-file Allure test report.

allure generate --single-file --clean --name "Dreams Test Report"

# Open the Allure test report.

allure open
