from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()

#random_password = fake.password(length=8, digits=True)
#random_email = fake.email()

def test_example(page: Page):
    page.goto('https://canvusapps.com/login')
    page.locator('#email').fill(fake.email()) # page.locator("#email").fill(random_email())
    page.locator('[name="password"]').fill(fake.password(length=8, digits=True))
    page.get_by_role(role='checkbox', name='Remember me').check()
    page.get_by_role(role='button', name='Login').click()
    expect(page).to_have_url('https://canvusapps.com/sessions')
    #assert page.locator('.alert-block').inner_text()== '1Invalid email or password'  # Assert w/o retry
    expect(page.locator('.alert-block')).to_have_text('Invalid email or password', timeout=8000)

