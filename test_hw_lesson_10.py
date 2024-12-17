from playwright.sync_api import Page, expect

def test_example(page: Page):
    page.goto('https://www.qa-practice.com/elements/select/mult_select')

    page.locator('[id="id_choose_the_place_you_want_to_go"]').select_option('Old town')
    place = page.locator('[id="id_choose_the_place_you_want_to_go"]')
    place.inner_text()
    page.locator('[id="id_choose_how_you_want_to_get_there"]').select_option('Bus')
    page.locator('[id="id_choose_when_you_want_to_go"]').select_option('Next week')
    page.locator('[id="submit-id-submit"]').click()
    expect(page.locator('[id="result-text"]')).to_have_text("to go by bus to the old town next week")

    # for running in Python terminal:

    # from playwright.sync_api import sync_playwright
    # playwright = sync_playwright().start()
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # # page = browser.new_page()
    # page.goto('https://www.qa-practice.com/elements/select/mult_select')
    # page.locator('[id="id_choose_the_place_you_want_to_go"]').select_option('Old town')
    # page.locator('[id="id_choose_how_you_want_to_get_there"]').select_option('Bus')
    # page.locator('[id="id_choose_when_you_want_to_go"]').select_option('Next week')
    # page.locator('[id="submit-id-submit"]').click()
    # # from playwright.sync_api import expect
    # expect(page.locator('[id="result-text"]')).to_have_text("to go by bus to the old town next week")