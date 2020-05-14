"""
pytest conftest file
"""

import os

# env
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="env option: dev/staging/live")
    parser.addoption("--headless", action="store", default="False", help="headless option: True/False")

def pytest_configure(config):
    env = config.getoption("env")
    os.environ["env"] = env if env else "dev"
    os.environ["headless"] = config.getoption("headless")


# Html Report
'''
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    #cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.now(), class_='col-time'))
    #cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
'''