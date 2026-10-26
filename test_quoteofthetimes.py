import re, pytest
from playwright.sync_api import Page, expect, Browser

@pytest.fixture (scope="module")
def quote(browser: Browser):
    context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
    page = context.new_page()
    page.goto("https://www.quoteofthetimes.com/")
    expect(page.locator("#quote")).not_to_be_empty(timeout=10000)

    yield page 
    
    context.close()

def test_has_title(quote: Page):
    
    expect(quote).to_have_title(re.compile("Quotes of the times"))

def test_background_appears(quote):
    background = quote.locator(".background-image")
    expect(background).to_have_css(
        "background-image", 
        'url("https://www.quoteofthetimes.com/wild-nature-7680x4320.jpg")'
    )

def test_has_text(quote):
    expect(quote.get_by_text("Daily Inspiration")).to_be_visible()

    expect(quote.get_by_text("Discover thousands of motivational, philosophical and famous quotes. Please use the view that is most comfortable for you 🙂")).to_be_visible()

def test_quote_show(quote):
    expect(quote.locator("#quote")).to_be_visible()

def test_time_show(quote):
    expect(quote.locator("#time")).to_be_visible()

def test_background_click(quote):
    quote.get_by_role("button", name="* Click for Alternate View *").click()
    background_2 = quote.locator(".background-image2")
    expect(background_2).to_have_css(
        "background-image", 'url("https://www.quoteofthetimes.com/Nature-image.jpg")'
    )
    expect(background_2).to_be_visible()

def test_copy(quote):
    shown = quote.locator("#quote").inner_text()
    assert shown.strip() != ""
    quote.get_by_role("button", name="📋 Copy").click()

    copied = quote.evaluate("navigator.clipboard.readText()")

    assert copied.strip() == shown.strip()

def test_like_button(quote):
    like = quote.get_by_role("button", name ="❤️ Like" )

    like.click()

    expect(quote.locator("#like-text")).not_to_have_text(re.compile(r"^\s*$"))

def test_socials(quote):

    expect(quote.locator(".fa-linkedin")).to_be_visible()

    expect(quote.locator(".fa-instagram")).to_be_visible()

    expect(quote.locator(".fa-github")).to_be_visible()

    






