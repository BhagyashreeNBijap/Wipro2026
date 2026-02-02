'''Question 6 – Browser Automation & Built-in Libraries (Coding) 
Topics Covered: SeleniumLibrary, Built-in library Write a Robot Framework test case that: 
1. Opens a browser using SeleniumLibrary
2. Interacts with: Text box, Radio button , Check box, Drop-down
3. Uses Built-in keywords: Run Keyword If'''

*** Settings ***
Library    SeleniumLibrary

Suite Setup     Open Test Browser
Suite Teardown  Close Browser


*** Variables ***
${URL}      https://testautomationpractice.blogspot.com/
${BROWSER}  chrome


*** Test Cases ***
Form Automation Test

    # 1. Open Browser (done in Suite Setup)
    # 2. Interact with Text Box
    Input Text    id=name      Bhagyashree
    Input Text    id=email     bhagyashree@gmail.com

    # 2. Interact with Radio Button
    Click Element    id=female

    # 2. Interact with Check Box
    Click Element    id=sunday

    # 2. Interact with Drop-down
    Select From List By Label    id=country    India

    # 3. Built-in keyword: Run Keyword If
    Run Keyword If    '${BROWSER}' == 'chrome'    Log    Running test on Chrome

    # Validation
    ${selected}=    Get Selected List Label    id=country
    Should Be Equal    ${selected}    India


*** Keywords ***
Open Test Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
