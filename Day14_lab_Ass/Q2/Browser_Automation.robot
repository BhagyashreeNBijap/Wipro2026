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

    # Text Box
    Input Text    id=name      Bhagyashree
    Input Text    id=email     bhagyashree@gmail.com

    # Radio Button
    Click Element    id=female

    # Check Box
    Click Element    id=sunday

    # Drop-down
    Select From List By Label    id=country    India

    # Built-in keyword: Sleep
    Sleep    2s

    # Built-in keyword: Run Keyword If
    Run Keyword If    '${BROWSER}' == 'chrome'    Log    Running test on Chrome browser

    # Screenshot
    Capture Page Screenshot

    # Validation (Form data validation)
    ${selected}=    Get Selected List Label    id=country
    Should Be Equal    ${selected}    India


*** Keywords ***
Open Test Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

