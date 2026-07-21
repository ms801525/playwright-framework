import re, pytest, time
from playwright.sync_api import Page, expect, Browser

@pytest.fixture (scope="module")
def toolkit(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.jsutilitytoolkit.com/")

    yield page 
    
    context.close()


def test_has_title(toolkit: Page):
    # Expect a title "to contain" a substring.
    expect(toolkit).to_have_title(re.compile("JavaScript Utility Toolkit V1"))
    time.sleep(2)

def test_empty_input(toolkit):
    toolkit.locator("#clear-button-json").click()
    toolkit.get_by_role("button", name="Calculate").click()
    expect(toolkit.get_by_text("Result: Not Valid, Please")).to_be_visible()
    time.sleep(2)

def test_empty_convert(toolkit):
    toolkit.get_by_role("button", name="Convert").click()
    expect(toolkit.get_by_text("Result: Not valid, need to")).to_be_visible()
    time.sleep(2)

def test_empty_analyze(toolkit):
    toolkit.get_by_role("button", name="Analyze").click()
    expect(toolkit.get_by_text("Result: Invalid Input. Enter")).to_be_visible()
    time.sleep(2)

def test_empty_format(toolkit):
    toolkit.get_by_role("button", name="Format").click()
    expect(toolkit.get_by_text("Invalid, first JSON key:value")).to_be_visible()
    time.sleep(2)

def test_empty_sqrt(toolkit):
    toolkit.locator("#operations").select_option("sqrt")
    toolkit.get_by_role("button", name="Calculate").click()
    expect(toolkit.get_by_text("Result: Not Valid, Please")).to_be_visible()
    time.sleep(2)


def test_add_calculate(toolkit):

    # try the first calculation
    toolkit.locator("#clear-button-json").click()
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("5")
    toolkit.locator("#input2").click()
    toolkit.locator("#input2").fill("5")
    toolkit.get_by_role("button", name="Calculate").click()

    # Expects toolkit to have a heading with the name of Installation.
    expect(toolkit.get_by_text("Result: 10")).to_be_visible()
    time.sleep(2)


def test_subtract_caculate(toolkit):
    toolkit.locator("#operations").select_option("subtract")
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("5")
    toolkit.locator("#input2").click()
    toolkit.locator("#input2").fill("5")
    toolkit.get_by_role("button", name="Calculate").click()

    #test result with substraction
    expect(toolkit.get_by_text("Result: 0")).to_be_visible()
    time.sleep(2)
    

def test_multiply_calculate(toolkit):
    toolkit.locator("#operations").select_option("multiply")
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("5")
    toolkit.locator("#input2").click()
    toolkit.locator("#input2").fill("5")
    toolkit.get_by_role("button", name="Calculate").click()

    #test result with multiplication
    expect(toolkit.get_by_text("Result: 25")).to_be_visible()
    time.sleep(2)


def test_divide_calculate(toolkit):
    toolkit.locator("#operations").select_option("divide")
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("10")
    toolkit.locator("#input2").click()
    toolkit.locator("#input2").fill("5")
    toolkit.get_by_role("button", name="Calculate").click()

    #test result with multiplication
    expect(toolkit.get_by_text("Result: 2")).to_be_visible()
    time.sleep(2)


def test_pow_calculate(toolkit):
    toolkit.locator("#operations").select_option("pow")
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("2")
    toolkit.locator("#input2").click()
    toolkit.locator("#input2").fill("4")
    toolkit.get_by_role("button", name="Calculate").click()

    #test result with multiplication
    expect(toolkit.get_by_text("Result: 16")).to_be_visible()
    time.sleep(2)

def test_sqrt_calculate(toolkit):
    toolkit.locator("#operations").select_option("sqrt")
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("49")
    toolkit.get_by_role("button", name="Calculate").click()

    #test result with multiplication
    expect(toolkit.get_by_text("Result: 7")).to_be_visible()
    time.sleep(2)











"""
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    toolkit = context.new_toolkit()
    toolkit.goto("https://www.jsutilitytoolkit.com/")
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("5")
    toolkit.locator("#input2").click()
    toolkit.locator("#input2").fill("5")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.locator("#operations").select_option("subtract")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.get_by_role("button", name="Copy").click()
    toolkit.locator("#operations").select_option("multiply")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.locator("#operations").select_option("divide")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("-5")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.locator("#operations").select_option("add")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.locator("#operations").select_option("subtract")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.locator("#operations").select_option("multiply")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("5")
    toolkit.locator("#operations").select_option("pow")
    toolkit.get_by_role("button", name="Calculate").click()
    toolkit.locator("#clear-button-json").click()


    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("55")
    toolkit.locator("#input2").click()
    toolkit.locator("#input2").fill("5")
    toolkit.locator("#clear-button-json").click()
    toolkit.locator("#input1").click()
    toolkit.locator("#input1").fill("55")
    toolkit.locator("#input2").click()
    toolkit.locator("#input2").fill("5")
    toolkit.locator("#operations").select_option("sqrt")
    toolkit.get_by_role("button", name="Calculate").click()


    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.get_by_placeholder("Enter value to be converted").fill("45")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("km-to-miles")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("celsius-to-fahrenheit")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("lbs-to-kg")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("miles-to-km")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("fahrenheit-to-celsius")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("feet-to-meters")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("meters-to-feet")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("liters-to-gallons")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("gallons-to-liters")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("inches-to-centimeters")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#unit-converter-select").select_option("centimeters-to-inches")
    toolkit.get_by_role("button", name="Convert").click()
    toolkit.locator("#clear-button-unit").click()


    toolkit.get_by_role("textbox", name="Enter text to be analyzed").click()
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").fill("hello")
    toolkit.get_by_role("button", name="Analyze").click()


    toolkit.get_by_role("textbox", name="Enter text to be analyzed").click()
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").fill("hello my name is mustafa")
    toolkit.get_by_role("button", name="Analyze").click()


    toolkit.get_by_role("textbox", name="Enter text to be analyzed").press("CapsLock")
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").click()
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").fill("HEllO MY NAME IS MUSTAFA")
    toolkit.get_by_role("button", name="Analyze").click()


    toolkit.locator("#text-analyzer-select").select_option("word-count")
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").click()
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").fill("hello my name is mustafa")
    toolkit.get_by_role("button", name="Analyze").click()

    toolkit.locator("#text-analyzer-select").select_option("sentence-count")
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").click()
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").fill("hello my name is mustafa")
    toolkit.get_by_role("button", name="Analyze").click()



    toolkit.locator("#text-analyzer-select").select_option("most-common-word")
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").click()
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").fill("hello my name is mustafa")
    toolkit.get_by_role("button", name="Analyze").click()


    toolkit.locator("#clear-button-analyzer").click()

    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").fill("Make")
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").fill("Honda")
    toolkit.locator("#json-formatter-input-2a").click()
    toolkit.locator("#json-formatter-input-2a").fill("Model")
    toolkit.locator("#json-formatter-input-2b").click()
    toolkit.locator("#json-formatter-input-2b").fill("Civic")
    toolkit.locator("#json-formatter-input-3a").click()
    toolkit.locator("#json-formatter-input-3a").fill("Year")
    toolkit.locator("#json-formatter-input-3b").click()
    toolkit.locator("#json-formatter-input-3b").fill("2016")
    toolkit.get_by_role("button", name="Format").click()
    toolkit.get_by_role("button", name="Copy").click()
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").click()
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").press("ControlOrMeta+v")
    toolkit.get_by_role("textbox", name="Enter text to be analyzed").fill("{\n  \"Make\": \"Honda\",\n  \"Model\": \"Civic\",\n  \"Year\": \"2016\"\n}")
    toolkit.get_by_role("button", name="Analyze").click()
    toolkit.locator("#clear-button-json").click()
    toolkit.get_by_role("button", name="Format").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
"""