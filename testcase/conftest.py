import os
import time

import pytest
from selenium import webdriver
import pytest_html


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("opening chrome browser")

    elif browser == "Firefox":
        driver = webdriver.Firefox()
        print("opening firefox browser")

    elif browser == "Edge":
        driver = webdriver.Edge()
        print("Opening edge browser")

    else:
        print("Headless mode")
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)

    driver.implicitly_wait(4)
    driver.maximize_window()
    return driver




# This hook is used to take automatically screenshot and place in HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call" or report.when == "setup":
        # always add url to report
        extras.append(pytest_html.extras.url("https://demo.nopcommerce.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            report.extras = extras


def pytest_html_report_title(report):
    report.title = "Nopcommerce Automation Report"
