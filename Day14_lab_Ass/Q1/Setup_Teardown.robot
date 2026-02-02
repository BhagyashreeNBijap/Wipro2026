*** Settings ***
Library    SeleniumLibrary

# (1) Suite Setup and Suite Teardown
Suite Setup       Suite Start
Suite Teardown    Suite End

# (2) Test Setup and Test Teardown
Test Setup        Test Start
Test Teardown     Test End


*** Variables ***
${URL}      https://example.com
${BROWSER}  chrome


*** Test Cases ***
# (5) Tagged test case
Open Example Website
    [Tags]    smoke
    Open Browser    ${URL}    ${BROWSER}
    Sleep    5s
    Title Should Be    Example Domain
    Close Browser

Simple Log Test
    [Tags]    sanity
    Log    This is a non-browser test case


*** Keywords ***
Suite Start
    Log    Suite execution started

Suite End
    Log    Suite execution finished

Test Start
    Log    Test execution started

Test End
    Log    Test execution finished
