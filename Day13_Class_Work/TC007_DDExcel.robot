*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    OrangeHRM Login With Excel
Suite Setup    Open OrangeHRM
Suite Teardown    Close OrangeHRM

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   chrome

*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}
    Wait Until Element Is Visible    name=username    15s
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    xpath=//button[@type='submit']
    Wait Until Element Is Visible    xpath=//span[@class='oxd-userdropdown-tab']    15s
    Capture Page Screenshot
    Logout From OrangeHRM

Logout From OrangeHRM
    Click Element    xpath=//span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible    xpath=//a[text()='Logout']    10s
    Click Element    xpath=//a[text()='Logout']
    Wait Until Element Is Visible    name=username    15s

Close OrangeHRM
    Close Browser

*** Test Cases ***
Login with user from Excel
    [Template]    OrangeHRM Login With Excel
    ${username}    ${password}
