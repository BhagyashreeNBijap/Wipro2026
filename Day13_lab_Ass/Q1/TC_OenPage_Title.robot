*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To Page
Suite Teardown    Close Browser


*** Variables ***
${BROWSER}    chrome
${URL}        https://www.google.com
${EXPECTED_TITLE}    Google


*** Keywords ***
Open Browser To Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    name=q    timeout=10s


*** Test Cases ***
Verify Page Title And Take Screenshot
    Title Should Be    ${EXPECTED_TITLE}
    Capture Page Screenshot
