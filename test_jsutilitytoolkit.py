import re, pytest, time
from playwright.sync_api import Page, expect, Browser

@pytest.fixture (scope="module")
def toolkit(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.jsutilitytoolkit.com/")

    yield page 
    
    context.close()

#THIS IS TO TEST THE BUTTON CLICK IN EMPTY TEXT BOXES 
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

#THIS IS FOR THE CALCULATOR FEATURE
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


#THIS IS FOR THE UNIT CONVERTER
def test_kg_lbs_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("kg-to-lbs")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 220.46")).to_be_visible()
    time.sleep(2)

def test_km_miles_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("km-to-miles")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 62.14")).to_be_visible()
    time.sleep(2)

def test_cel_fah_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("celsius-to-fahrenheit")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 212.00")).to_be_visible()
    time.sleep(2)

def test_lbs_kg_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("lbs-to-kg")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 45.36")).to_be_visible()
    time.sleep(2)

def test_miles_km_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("miles-to-km")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 160.93")).to_be_visible()
    time.sleep(2)

def test_fah_cel_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("fahrenheit-to-celsius")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 37.78")).to_be_visible()
    time.sleep(2)

def test_meters_feet_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("meters-to-feet")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 328.08")).to_be_visible()
    time.sleep(2)

def test_feer_meters_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("feet-to-meters")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 30.48")).to_be_visible()
    time.sleep(2)

def test_liters_gallons_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("liters-to-gallons")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 26.42")).to_be_visible()
    time.sleep(2)

def test_gallons_liters_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("gallons-to-liters")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 378.54")).to_be_visible()
    time.sleep(2)

def test_inches_cm_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("inches-to-centimeters")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 254.00")).to_be_visible()
    time.sleep(2)

def test_cm_inches_convert(toolkit):
    toolkit.locator("#unit-converter-select").select_option("centimeters-to-inches")
    toolkit.get_by_placeholder("Enter value to be converted").click()
    toolkit.locator("#unit-converter-input").fill("100")
    toolkit.locator("#unit-converter-button").click()
    toolkit.get_by_role("button", name="Convert").click()

    expect(toolkit.get_by_text("Result: 39.37")).to_be_visible()
    time.sleep(2)



#THIS IS FOR THE TEXT ANALYZER

def test_char_count_analyze(toolkit):
    toolkit.locator("#text-analyzer-select").select_option("char-count")
    toolkit.get_by_placeholder("Enter text to be analyzed").click()
    toolkit.locator("#text-analyzer-input").fill("Hello, My name is John. I live in New York.")
    toolkit.get_by_role("button", name = "Analyze").click()

    expect(toolkit.get_by_text("Result: 43"))
    time.sleep(2)

def test_word_count_analyze(toolkit):
    toolkit.locator("#text-analyzer-select").select_option("word-count")
    toolkit.get_by_placeholder("Enter text to be analyzed").click()
    toolkit.locator("#text-analyzer-input").fill("Hello, My name is John. I live in New York.")
    toolkit.get_by_role("button", name = "Analyze").click()

    expect(toolkit.get_by_text("Result: 10"))
    time.sleep(2)

def test_sen_count_analyze(toolkit):
    toolkit.locator("#text-analyzer-select").select_option("sentence-count")
    toolkit.get_by_placeholder("Enter text to be analyzed").click()
    toolkit.locator("#text-analyzer-input").fill("Hello, My name is John. I live in New York.")
    toolkit.get_by_role("button", name = "Analyze").click()

    expect(toolkit.get_by_text("Result: 2"))
    time.sleep(2)

def test_common_word_analyze(toolkit):
    toolkit.locator("#text-analyzer-select").select_option("most-common-word")
    toolkit.get_by_placeholder("Enter text to be analyzed").click()
    toolkit.locator("#text-analyzer-input").fill("Hello I am john. Hello I am Jason. Hello I am Jack. Hey I am Kat. Hey you are Kurt. Hello you are Sam. Hello this is Kurtis")
    toolkit.get_by_role("button", name = "Analyze").click()

    expect(toolkit.get_by_text("Result: hello"))
    time.sleep(2)
    
    
#THIS IS FOR THE JSON FORMATTER
def test_first_key_pair(toolkit):

    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").fill("Make")
    toolkit.get_by_role("button", name="Format").click()

    expect(toolkit.get_by_text("Invalid, first JSON key:value"))
    time.sleep(2)

def test_first_value(toolkit):
    toolkit.locator("#clear-button-json").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").fill("Honda")
    toolkit.get_by_role("button", name="Format").click()

    expect(toolkit.get_by_text("Invalid, first JSON key:value"))
    time.sleep(2)

def test_first_key_value_pair(toolkit):
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").fill("Make")
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").fill("Honda")
    toolkit.get_by_role("button", name="Format").click()

    expect(toolkit.get_by_text("{ \"Make\": \"Honda\" }"))
    time.sleep(2)
    
def test_2_key_value_pair(toolkit):
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").fill("Make")
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").fill("Honda")

    toolkit.locator("#json-formatter-input-2a").click()
    toolkit.locator("#json-formatter-input-2a").fill("Model")

    toolkit.locator("#json-formatter-input-2b").click()
    toolkit.locator("#json-formatter-input-2b").fill("Civic")

    toolkit.get_by_role("button", name="Format").click()

    expect(toolkit.get_by_text("{ \"Make\": \"Honda\", \"Model\": \""))
    time.sleep(2)

def test_3_key_value_pair(toolkit):
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").fill("Make")
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").fill("Honda")

    toolkit.locator("#json-formatter-input-2a").click()
    toolkit.locator("#json-formatter-input-2a").fill("Model")

    toolkit.locator("#json-formatter-input-2b").click()
    toolkit.locator("#json-formatter-input-2b").fill("Civic")

    toolkit.locator("#json-formatter-input-3a").fill("Year")
    toolkit.locator("#json-formatter-input-3b").click()
    toolkit.locator("#json-formatter-input-3b").fill("2016")
    toolkit.get_by_role("button", name="Format").click()

    toolkit.get_by_role("button", name="Format").click()

    expect(toolkit.get_by_text("{ \"Make\": \"Honda\", \"Model\": \""))
    time.sleep(2)

def test_key_value_copy(toolkit):
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter title (e.g").fill("Make")
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").click()
    toolkit.get_by_role("textbox", name="(REQUIRED) Enter text for to").fill("Honda")

    toolkit.locator("#json-formatter-input-2a").click()
    toolkit.locator("#json-formatter-input-2a").fill("Model")

    toolkit.locator("#json-formatter-input-2b").click()
    toolkit.locator("#json-formatter-input-2b").fill("Civic")

    toolkit.locator("#json-formatter-input-3a").fill("Year")
    toolkit.locator("#json-formatter-input-3b").click()
    toolkit.locator("#json-formatter-input-3b").fill("2016")
    toolkit.get_by_role("button", name="Format").click()

    toolkit.get_by_role("button", name="Format").click()
    toolkit.get_by_role("button", name="Copy").click()

    toolkit.locator("#text-analyzer-input").fill("{\n  \"Make\": \"Honda\",\n  \"Model\": \"Civic\",\n  \"Year\": \"2016\"\n}")

    expect(toolkit.get_by_text("{ \"Make\": \"Honda\", \"Model\": \""))
    time.sleep(2)















