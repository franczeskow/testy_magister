*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.pepper.pl/
${EMAIL}    tescicki123
${PASSWORD}    tajnehaslo123
${ALERT}    telefony
${COMMENT}    Fajna okazja

*** Test Cases ***
Login And Create Alert
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//*[text()=" Akceptuj wszystkie "]
    Click Element    xpath=//*[text()=" Akceptuj wszystkie "]
    Click Element    xpath=//button[@class='button--toW5-square space--ml-2 button button--shape-circle button--type-primary button--mode-white']
    Wait Until Element Is Visible    xpath=//input[@placeholder='jan@kowalski.pl']
    Input Text    xpath=//input[@placeholder='jan@kowalski.pl']    ${EMAIL}
    Click Element    xpath=//span[contains(text(), 'Kontynuuj')]
    Wait Until Element Is Visible    xpath=//input[@placeholder='**************']
    Input Text    xpath=//input[@placeholder='**************']    ${PASSWORD}
    Click Element    xpath=//span[text()=' Zaloguj Się ']
    Wait Until Element Is Visible    xpath=//img[@alt="Awatar użytkownika ${EMAIL}"]

    # Navigate to alerts
    Click Element    xpath=//img[@alt="Awatar użytkownika ${EMAIL}"]
    Click Element    xpath=//a[text()=" Lista alertów "]
    Click Element    xpath=//span[text()="Zarządzaj alertami"]
    Input Text    xpath=//input[@placeholder='Twój alert...']    ${ALERT}
    Wait Until Element Is Visible    xpath=//ol/li/div/span[text()=" Telefony "]
    Click Element    xpath=//ol/li/div/span[text()=" Telefony "]
    Click Element    xpath=//span[contains(text(), 'Utwórz nowy alert')]
    Wait Until Element Is Visible    xpath=//span[contains(text(), '${ALERT}')]

    Close Browser

Login And Comment
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//*[text()=" Akceptuj wszystkie "]
    Click Element    xpath=//*[text()=" Akceptuj wszystkie "]
    Click Element    xpath=//button[@class='button--toW5-square space--ml-2 button button--shape-circle button--type-primary button--mode-white']
    Wait Until Element Is Visible    xpath=//input[@placeholder='jan@kowalski.pl']
    Input Text    xpath=//input[@placeholder='jan@kowalski.pl']    ${EMAIL}
    Click Element    xpath=//span[contains(text(), 'Kontynuuj')]
    Wait Until Element Is Visible    xpath=//input[@placeholder='**************']
    Input Text    xpath=//input[@placeholder='**************']    ${PASSWORD}
    Click Element    xpath=//span[text()=' Zaloguj Się ']
    Wait Until Element Is Visible    xpath=//img[@alt="Awatar użytkownika ${EMAIL}"]

    # Comment
    Click Element    xpath=(//a[@data-t="threadLink"])[1]
    Wait Until Element Is Visible    xpath=//div[@placeholder="O czym teraz myślisz..."]
    Click Element    xpath=//div[@placeholder="O czym teraz myślisz..."]
    Wait Until Element Is Visible    xpath=//div[@contenteditable="true"]
    Input Text    xpath=//div[@contenteditable="true"]    ${COMMENT}
    Click Element    xpath=//span[text()="Skomentuj"]
    Wait Until Element Is Visible    xpath=//div[@class="comment-body"]/div/div[text()="${COMMENT}"]

    Close Browser