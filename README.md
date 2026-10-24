# Playwright test framework

End-to-end tests, written in Python with Playwright and pytest, for two of my live web apps:

| Site | Test file | Tests | What they cover |
| --- | --- | --- | --- |
| [Quote of the Times](https://www.quoteofthetimes.com) ([code](https://github.com/ms801525/Quote-of-the-Times)) | `test_quoteofthetimes.py` | 9 | Page title and text, background images and the alternate view, the quote and clock, copy and like buttons, social links |
| [JS Utility Toolkit](https://www.jsutilitytoolkit.com) ([code](https://github.com/ms801525/javascript-toolkit)) | `test_jsutilitytoolkit.py` | 34 | Empty-input validation for every tool, all six calculator operations, twelve unit conversions, the text analyzer and the JSON formatter |

The tests run against the live sites, so they check what users actually see after each deployment.

## Run them

```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest --browser chromium
```

Add `--headed` to watch the browser, or `--html=report.html --self-contained-html` for an HTML report.

GitHub Actions runs the full suite on every push and saves the HTML report as a downloadable artifact.

## Built with

Python, pytest, Playwright, pytest-html, GitHub Actions.
