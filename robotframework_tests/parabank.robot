*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${PAGE_URL}      https://parabank.parasoft.com/
${BROWSER}        Chrome

*** Test Cases ***
Go to Parabank Page And Login
    Open Browser    browser=${BROWSER}
    Go To   ${PAGE_URL}
    Wait Until Page Contains Element   name:username
    Input Text    name:username    aaa
    Input Text    name:password    aaa
    Click Element    xpath://input[@value="Log In"]
    Wait Until Page Contains    Welcome aaa aaa