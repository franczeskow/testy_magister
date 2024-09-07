from playwright.sync_api import Page, expect

def test_pepper_alert(page: Page):
    page.goto("https://www.pepper.pl/")
    page.get_by_role("button", name="Akceptuj wszystkie").click()
    page.get_by_role("button", name="Zarejestruj się / Zaloguj Się").click()
    page.get_by_placeholder("jan@kowalski.pl").fill("tescicki123")
    page.get_by_role("button", name="Kontynuuj").click()
    page.get_by_placeholder("**************").fill("tajnehaslo123")
    page.get_by_role("button", name="Zaloguj Się", exact=True).click()
    expect(page.get_by_role("button", name="Awatar użytkownika tescicki123")).to_be_visible()


    page.get_by_role("button", name="Awatar użytkownika tescicki123").click()
    page.get_by_role("link", name="Lista alertów").click()
    page.get_by_role("link", name="Zarządzaj alertami").click()
    page.get_by_placeholder("Twój alert...").click()
    page.get_by_placeholder("Twój alert...").fill("telefony")
    page.locator("ol").filter(has_text="Telefony Telefony i smartfony").locator("div").first.click()
    page.get_by_role("button", name="Utwórz nowy alert").click()
    expect(page.get_by_role("button", name="telefony")).to_be_visible()




def test_pepper_comment(page: Page):
    page.goto("https://www.pepper.pl/")
    page.get_by_role("button", name="Akceptuj wszystkie").click()
    page.get_by_role("button", name="Zarejestruj się / Zaloguj Się").click()
    page.get_by_placeholder("jan@kowalski.pl").fill("tescicki123")
    page.get_by_role("button", name="Kontynuuj").click()
    page.get_by_placeholder("**************").fill("tajnehaslo123")
    page.get_by_role("button", name="Zaloguj Się", exact=True).click()
    expect(page.get_by_role("button", name="Awatar użytkownika tescicki123")).to_be_visible()


    page.locator('(//strong[@class="thread-title "])[1]').click()
    page.locator('//*[@placeholder="O czym teraz myślisz..."]').first.click()
    page.locator('//*[@contenteditable="true"]').first.fill("fajna okazja")
    page.get_by_role("button", name="Skomentuj").click()
    expect(page.get_by_text("fajna okazja")).to_be_visible() 