*** Settings ***
Resource    resources/keywords.robot
Resource    resources/testdata.robot
Suite Setup     Create API Session

*** Test Cases ***
Create Restaurant Positive
    ${response}=    Create Restaurant    ${RESTAURANT_DATA}
    Status Should Be    201    ${response}

Create Restaurant Negative
    ${invalid}=    Create Dictionary    category=Indian
    ${response}=    Create Restaurant    ${invalid}
    Status Should Be    400    ${response}
