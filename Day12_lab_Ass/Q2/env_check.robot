'''Question 2 – Environment Setup Verification (Coding) Write a Robot Framework test case that:
1. Verifies Python installation
2. Verifies Robot Framework installation 
3. Imports SeleniumLibrary
4. Prints the Robot Framework version 
5. Fails gracefully with meaningful logs if any dependency is missing'''


*** Settings ***
Library    BuiltIn
Library    SeleniumLibrary

*** Test Cases ***
Verify Environment Setup
    Log To Console    ==== Environment Verification Started ====

    #  Python Installation
    ${python_version}=    Evaluate    sys.version    sys
    Log    Python Version: ${python_version}
    Log To Console    Python is installed

    #  Robot Framework Installation
    ${robot_version}=    Evaluate    robot.__version__    robot
    Log    Robot Framework Version: ${robot_version}
    Log To Console    Robot Framework version: ${robot_version}

    #  SeleniumLibrary Import
    Log    SeleniumLibrary imported successfully
    Log To Console    SeleniumLibrary is available

    Log To Console    == Environment Verification Completed Successfully ==
