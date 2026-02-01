*** Settings ***
Library           SeleniumLibrary
Library           DateTime
Library           DataDriver    file=./testdata1.xlsx    sheet_name=Sheet1
Test Template     Register TutorialsNinja User
Test Setup        Open Registration Page
Test Teardown     Close Browser

*** Variables ***
${URL}      https://tutorialsninja.com/demo/index.php?route=account/register
${BROWSER}  chrome

*** Keywords ***
Open Registration Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=input-firstname    10s

Register TutorialsNinja User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}    ${confirm}    ${newsletter}

    # Generate a unique Gmail-style email
    ${time}          Get Current Date    result_format=%H%M%S
    ${final_email}   Set Variable        ${email}${time}@gmail.com

    Input Text    id=input-firstname    ${firstname}
    Input Text    id=input-lastname     ${lastname}
    Input Text    id=input-email        ${final_email}
    Input Text    id=input-telephone    ${telephone}
    Input Text    id=input-password     ${password}
    Input Text    id=input-confirm      ${confirm}

    Run Keyword If    '${newsletter}'=='yes'    Click Element    xpath=//input[@name='newsletter' and @value='1']
    Run Keyword If    '${newsletter}'=='no'     Click Element    xpath=//input[@name='newsletter' and @value='0']

    Click Element    name=agree
    Click Button     xpath=//input[@value='Continue']

    Wait Until Page Contains    Your Account Has Been Created!    10s
    Capture Page Screenshot

*** Test Cases ***
# This is required for PyCharm plugin to recognize tests
Register User Using Excel
    [Template]    Register TutorialsNinja User

# Dummy test to satisfy PyCharm
Dummy Test
    Log    PyCharm requires at least one static test
