import re
from playwright.sync_api import Playwright, sync_playwright, Page, expect


def test_checkbox(page: Page):
    page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    page.get_by_label("One").check()
    page.get_by_label("One").check()
    page.get_by_label("One").check()
    page.locator("#div_id_checkboxes div").nth(3).click()
    page.get_by_label("Two").check()
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("Selected checkboxes:").click()
    page.get_by_text("one, two, three").click()
    page.get_by_text("Selected checkboxes: one, two").click()
    page.get_by_text("Selected checkboxes:").click()
    expect(page.locator("img")).to_be_visible()
    expect(page.locator("#result-text")).to_match_aria_snapshot("- paragraph: one, two, three")
    expect(page.get_by_text("Three", exact=True)).to_be_visible()
