import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.jsutilitytoolkit.com/")
    page.locator("#input1").click()
    page.locator("#input1").fill("5")
    page.locator("#input2").click()
    page.locator("#input2").fill("5")
    page.get_by_role("button", name="Calculate").click()
    page.locator("#operations").select_option("subtract")
    page.get_by_role("button", name="Calculate").click()
    page.get_by_role("button", name="Copy").click()
    page.locator("#operations").select_option("multiply")
    page.get_by_role("button", name="Calculate").click()
    page.locator("#operations").select_option("divide")
    page.get_by_role("button", name="Calculate").click()
    page.locator("#input1").click()
    page.locator("#input1").fill("-5")
    page.get_by_role("button", name="Calculate").click()
    page.locator("#operations").select_option("add")
    page.get_by_role("button", name="Calculate").click()
    page.locator("#operations").select_option("subtract")
    page.get_by_role("button", name="Calculate").click()
    page.locator("#operations").select_option("multiply")
    page.get_by_role("button", name="Calculate").click()
    page.locator("#input1").click()
    page.locator("#input1").fill("5")
    page.locator("#operations").select_option("pow")
    page.get_by_role("button", name="Calculate").click()
    page.locator("#clear-button-json").click()


    page.locator("#input1").click()
    page.locator("#input1").fill("55")
    page.locator("#input2").click()
    page.locator("#input2").fill("5")
    page.locator("#clear-button-json").click()
    page.locator("#input1").click()
    page.locator("#input1").fill("55")
    page.locator("#input2").click()
    page.locator("#input2").fill("5")
    page.locator("#operations").select_option("sqrt")
    page.get_by_role("button", name="Calculate").click()


    page.get_by_placeholder("Enter value to be converted").click()
    page.get_by_placeholder("Enter value to be converted").fill("45")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("km-to-miles")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("celsius-to-fahrenheit")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("lbs-to-kg")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("miles-to-km")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("fahrenheit-to-celsius")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("feet-to-meters")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("meters-to-feet")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("liters-to-gallons")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("gallons-to-liters")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("inches-to-centimeters")
    page.get_by_role("button", name="Convert").click()
    page.locator("#unit-converter-select").select_option("centimeters-to-inches")
    page.get_by_role("button", name="Convert").click()
    page.locator("#clear-button-unit").click()

    
    page.get_by_role("textbox", name="Enter text to be analyzed").click()
    page.get_by_role("textbox", name="Enter text to be analyzed").fill("hello")
    page.get_by_role("button", name="Analyze").click()


    page.get_by_role("textbox", name="Enter text to be analyzed").click()
    page.get_by_role("textbox", name="Enter text to be analyzed").fill("hello my name is mustafa")
    page.get_by_role("button", name="Analyze").click()


    page.get_by_role("textbox", name="Enter text to be analyzed").press("CapsLock")
    page.get_by_role("textbox", name="Enter text to be analyzed").click()
    page.get_by_role("textbox", name="Enter text to be analyzed").fill("HEllO MY NAME IS MUSTAFA")
    page.get_by_role("button", name="Analyze").click()


    page.locator("#text-analyzer-select").select_option("word-count")
    page.get_by_role("textbox", name="Enter text to be analyzed").click()
    page.get_by_role("textbox", name="Enter text to be analyzed").fill("hello my name is mustafa")
    page.get_by_role("button", name="Analyze").click()

    page.locator("#text-analyzer-select").select_option("sentence-count")
    page.get_by_role("textbox", name="Enter text to be analyzed").click()
    page.get_by_role("textbox", name="Enter text to be analyzed").fill("hello my name is mustafa")
    page.get_by_role("button", name="Analyze").click()



    page.locator("#text-analyzer-select").select_option("most-common-word")
    page.get_by_role("textbox", name="Enter text to be analyzed").click()
    page.get_by_role("textbox", name="Enter text to be analyzed").fill("hello my name is mustafa")
    page.get_by_role("button", name="Analyze").click()


    page.locator("#clear-button-analyzer").click()

    page.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").click()
    page.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").fill("Make")
    page.get_by_role("textbox", name="(REQUIRED) Enter text for to").click()
    page.get_by_role("textbox", name="(REQUIRED) Enter text for to").fill("Honda")
    page.locator("#json-formatter-input-2a").click()
    page.locator("#json-formatter-input-2a").fill("Model")
    page.locator("#json-formatter-input-2b").click()
    page.locator("#json-formatter-input-2b").fill("Civic")
    page.locator("#json-formatter-input-3a").click()
    page.locator("#json-formatter-input-3a").fill("Year")
    page.locator("#json-formatter-input-3b").click()
    page.locator("#json-formatter-input-3b").fill("2016")
    page.get_by_role("button", name="Format").click()
    page.get_by_role("button", name="Copy").click()
    page.get_by_role("textbox", name="Enter text to be analyzed").click()
    page.get_by_role("textbox", name="Enter text to be analyzed").press("ControlOrMeta+v")
    page.get_by_role("textbox", name="Enter text to be analyzed").fill("{\n  \"Make\": \"Honda\",\n  \"Model\": \"Civic\",\n  \"Year\": \"2016\"\n}")
    page.get_by_role("button", name="Analyze").click()
    page.locator("#clear-button-json").click()
    page.get_by_role("button", name="Format").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)