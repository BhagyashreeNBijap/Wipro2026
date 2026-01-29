*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
open application
    open browser     https://www.google.com    chrome
    maximize browser window

*** Test Cases ***
TC002.robot
    open application
    title should be     Google
    Close Browser

