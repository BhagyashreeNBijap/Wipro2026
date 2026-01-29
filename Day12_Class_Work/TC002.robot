*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TC001.robot
     Open Browser    https://www.google.com    chrome
     Title Should Be    Google
     Close Browser
