from playwright.sync_api import Page, expect
import time

 def test_transfer_money(page: Page):
    #logowanie
    page.goto("http://localhost:3000/")
    page.get_by_label("Username").fill("Heath93")
    page.get_by_label("Password").fill("s3cret")
    page.locator("[data-test=\"signin-submit\"]").click()
    expect(page.locator("[data-test=\"sidenav-user-full-name\"]")).to_contain_text("Ted P")
    expect(page.locator("[data-test=\"sidenav-user-settings\"]")).to_contain_text("My Account")

    account_balance = page.locator("[data-test=\"sidenav-user-balance\"]").text_content()
    account_balance_parsed = float(account_balance.replace("$", "").replace(",", ""))

    page.locator("[data-test=\"nav-top-new-transaction\"]").click()
    page.get_by_text("Kristian Bradtke").click()
    page.get_by_placeholder("Amount").fill("$100")
    page.get_by_placeholder("Add a note").fill("przelew")
    page.locator("[data-test=\"transaction-create-submit-payment\"]").click()
    time.sleep(1)
    account_balance_2 = page.locator("[data-test=\"sidenav-user-balance\"]").text_content()
    account_balance_2_parsed = float(account_balance_2.replace("$", "").replace(",", ""))
    if account_balance_parsed != account_balance_2_parsed+100:
        raise(ValueError("Account value is not correct!"))

    page.locator("[data-test=\"sidenav-signout\"]").click()
    page.get_by_label("Username").fill("Arvilla_Hegmann")
    page.get_by_label("Password").fill("s3cret")
    page.locator("[data-test=\"signin-submit\"]").click()
    page.locator("[data-test=\"nav-personal-tab\"]").click()
    page.locator("[data-test*=\"transaction-action\"]").first.click()
    expect(page.locator("[data-test*=\"transaction-item-\"]")).to_contain_text("Ted Parisian paid Kristian Bradtke")
    page.locator("[data-test*=\"transaction-amount\"]").click()
    expect(page.locator("[data-test*=\"transaction-amount\"]")).to_contain_text("-$100.00")


def test_create_delete_account(page: Page):
    page.goto("http://localhost:3000/")
    page.get_by_label("Username").fill("Heath93")
    page.get_by_label("Password").fill("s3cret")
    page.locator("[data-test=\"signin-submit\"]").click()
    expect(page.locator("[data-test=\"sidenav-user-full-name\"]")).to_contain_text("Ted P")
    expect(page.locator("[data-test=\"sidenav-user-settings\"]")).to_contain_text("My Account") 
    
    page.locator("[data-test=\"sidenav-bankaccounts\"]").click()
    page.locator("[data-test=\"bankaccount-new\"]").click()
    page.get_by_placeholder("Bank Name").fill("nowe konto")
    page.get_by_placeholder("Routing Number").fill("999999999")
    page.get_by_placeholder("Account Number").fill("000000000")
    page.locator("[data-test=\"bankaccount-submit\"]").click()
    last_table_account_item = page.locator('[data-test*="bankaccount-list-item"]').last
    expect(last_table_account_item).to_contain_text("nowe konto")
    page.locator('[data-test*="bankaccount-list-item"] >div>div> button').last.click()
    expect(last_table_account_item).to_contain_text("nowe konto (Deleted)")