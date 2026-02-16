*** Settings ***
Resource    resources/keywords.robot
Resource    resources/testdata.robot
Suite Setup     Create API Session

*** Test Cases ***
Register User Positive
    ${response}=    Create User    ${USER_DATA}
    Status Should Be    201    ${response}

Register User Negative
    ${invalid}=    Create Dictionary    name=OnlyName
    ${response}=    Create User    ${invalid}
    Status Should Be    400    ${response}
