from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://parabank.parasoft.com/")
    page.locator('//input[@name="username"]').fill("aaa")
    page.locator('//input[@name="password"]').fill("aaa")
    page.get_by_text("Log In").click()
    expect(page.locator('//p[@class="smallText"]')).to_have_text("Welcome aaa aaa")