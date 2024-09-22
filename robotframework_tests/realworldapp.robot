*** Settings ***
Library    SeleniumLibrary
Library     String

*** Variables ***
${URL}    http://localhost:3000/
${USERNAME}    Heath93
${PASSWORD}    s3cret
${USERNAME_2}    Arvilla_Hegmann
${TRANSACTION_AMOUNT}    $100
${NOTE}    przelew
${BANK_NAME}    nowe konto
${ROUTING_NUMBER}    999999999
${ACCOUNT_NUMBER}    000000000


*** Test Cases ***

Full User Workflow
    Open Browser    ${URL}    chrome    options=add_argument("-disable-search-engine-choice-screen")
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    css=[data-test='signin-submit']
    Wait Until Element Is Visible    css=[data-test='sidenav-user-full-name']
    Element Should Contain   css=[data-test='sidenav-user-full-name']    Ted P
    Element Should Contain       css=[data-test='sidenav-user-settings']    My Account

    ${initial_balance}=    Get Text    css=[data-test='sidenav-user-balance']
    ${initial_balance}=    Replace String    ${initial_balance}    $    ${EMPTY}	
    ${initial_balance}=    Replace String    ${initial_balance}    ,    ${EMPTY}	
    ${initial_balance}=    Convert To Number    ${initial_balance}
    
    Click Element    css=[data-test='nav-top-new-transaction']
    Click Element    xpath=//span[text()="Kristian Bradtke"]
    Input Text    css=[placeholder='Amount']    ${TRANSACTION_AMOUNT}
    Input Text    css=[placeholder='Add a note']    ${NOTE}
     Click Element    css=[data-test='transaction-create-submit-payment']
    Sleep    1

    ${updated_balance}=    Get Text    css=[data-test='sidenav-user-balance']
    ${updated_balance}=    Replace String    ${updated_balance}    $    ${EMPTY}	
    ${updated_balance}=    Replace String    ${updated_balance}    ,    ${EMPTY}	
    ${updated_balance}=    Convert To Number    ${updated_balance}
    
    ${expected_balance}=    Evaluate    ${initial_balance} - 100
    Should Be Equal As Numbers    ${expected_balance}    ${updated_balance}

     Click Element    css=[data-test='sidenav-signout']
    Input Text    id=username    ${USERNAME_2}
    Input Text    id=password    ${PASSWORD}
     Click Element    css=[data-test='signin-submit']
    Wait Until Element Is Visible    css=[data-test='nav-personal-tab']
     Click Element    css=[data-test='nav-personal-tab']
    Click Element    css=[data-test*='transaction-action']
    Element Should Contain    css=[data-test*='transaction-item-']    Ted Parisian paid Kristian Bradtke
    Click Element    css=[data-test*='transaction-amount']
    Element Should Contain   css=[data-test*='transaction-amount']    -$100.00
    Close Browser

Bank Account Management
    Open Browser    ${URL}    chrome    options=add_argument("-disable-search-engine-choice-screen")
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    css:[data-test='signin-submit']
    Wait Until Element Is Visible    css:[data-test='sidenav-user-full-name']
    Click Link    css:[data-test='sidenav-bankaccounts']
    Click Element    css:[data-test='bankaccount-new']
    Input Text    css:input[placeholder="Bank Name"]    ${BANK_NAME}
    Input Text    css:input[placeholder="Routing Number"]    ${ROUTING_NUMBER}
    Input Text    css:input[placeholder="Account Number"]    ${ACCOUNT_NUMBER}
    Click Element    css:[data-test='bankaccount-submit']
    ${last_account}    Wait Until Element Is Visible    css:[data-test*="bankaccount-list-item"]:last-child
    Element Should Contain    css:[data-test*="bankaccount-list-item"]:last-child    ${BANK_NAME}
    Wait Until Element Is Visible    css:[data-test*="bankaccount-list-item"]:last-child > div > div > button
    Click Element    css:[data-test*="bankaccount-list-item"]:last-child > div > div > button
    ${last_account_deleted}    Wait Until Element Is Visible    css:[data-test*="bankaccount-list-item"]:last-child
    Element Should Contain    css:[data-test*="bankaccount-list-item"]:last-child    ${BANK_NAME} (Deleted)
    Close Browser