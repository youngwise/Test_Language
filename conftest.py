from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')

    if language is None:
        raise pytest.UsageError('--language should be don\'t None!')

    option = Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': language})

    print('\nStart browser for test...')
    browser = webdriver.Chrome(options=option)
    browser.implicitly_wait(5)
    yield browser
    print('\nquit browser...')
    browser.quit()
