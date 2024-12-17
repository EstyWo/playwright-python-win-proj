from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()
#random_password = fake.password(length=8, digits=True)
#random_email = fake.email()

# def test_example(page: Page):
#     page.goto('https://canvusapps.com/login')
#     page.locator('#email').fill(fake.email()) # page.locator("#email").fill(random_email())
#     page.locator('[name="password"]').fill(fake.password(length=8, digits=True))
#     page.get_by_role(role='checkbox', name='Remember me').check()
#     page.get_by_role(role='button', name='Login').click()
#     expect(page).to_have_url('https://canvusapps.com/sessions')
#     #assert page.locator('.alert-block').inner_text()== '1Invalid email or password'  # Assert w/o retry
#     expect(page.locator('.alert-block')).to_have_text('Invalid email or password', timeout=8000)

def test_sign_up(page: Page):
    random_name = fake.name()
    random_email = fake.email()
    random_password = fake.password()
    random_company = fake.company()
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto('https://canvusapps.com/signup')
    page.locator("#user_name").fill(random_name)
    page.locator("#user_email").fill(random_email)
    page.locator("#user_password").fill(random_password)
    page.locator("#user_password_confirmation").fill(random_password)
    page.locator("#company_name").fill(random_company)
    page.get_by_role(role="button", name="Sign up").click()
    expect(page).to_have_url('https://canvusapps.com/register')
    expect(page.get_by_role("heading", name="Congratulations!")).to_be_visible()
    expect(page.get_by_role("heading", name="Congratulations!")).to_have_text("Congratulations!", timeout=8000)