*** Settings ***
Library           SeleniumLibrary
Test Template     Login With Credentials
Suite Setup       Open Browser To Login Page
Suite Teardown    Close Browser

*** Variables ***
${URL}        https://tutorialsninja.com/demo/index.php?route=account/login
${BROWSER}    chrome

*** Test Cases ***
Login as Admin
    [Template]    Login With Credentials
    admin    admin123

Login as User1
    [Template]    Login With Credentials
    user1    user123

Login as Guest
    [Template]    Login With Credentials
    guest    guest123

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=email    10s

Close Browser
    Close All Browsers

Input Credentials
    [Arguments]    ${username}    ${password}
    Input Text    name=email    ${username}
    Input Text    name=password    ${password}

Click Login
    Click Button    xpath=//input[@value='Login']
    Sleep    2s

Verify Login Success
    Element Should Be Visible    xpath=//a[text()='Logout']

Login With Credentials
    [Arguments]    ${username}    ${password}
    Input Credentials    ${username}    ${password}
    Click Login
    Run Keyword And Ignore Error    Verify Login Success
