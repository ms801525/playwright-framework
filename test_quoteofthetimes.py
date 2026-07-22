import re, pytest, time
from playwright.sync_api import Page, expect, Browser

@pytest.fixture (scope="module")
def toolkit(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.quoteofthetimes.com/")

    yield page 
    
    context.close()
