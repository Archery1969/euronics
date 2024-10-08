behave -D ENV=Prod
allure generate --single-file --clean --name "Dreams Test Report"
allure open