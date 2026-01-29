'''Topics Covered: Introduction to Robot Framework
Write a Robot Framework test suite (.robot file) that: 
1. Uses the BuiltIn library 
2. Contains at least two test cases 
3. Logs messages using Log and Log To Console 
4. Demonstrates the use of variables (scalar and list) 
5. Executes successfully using the robot command'''


*** Settings ***
Library    BuiltIn

*** Variables ***
${name}        Bhagyashree
${age}         22
@{colors}      Red    Green    Blue

*** Test Cases ***
TC1_Print User Details
    Log    User name is: ${name}
    Log To Console    Age is: ${age}
    Log To Console    Favorite colors: ${colors}

TC2_List Demonstration
    Log    First color is: ${colors}[0]
    Log To Console    Second color is: ${colors}[1]
    Log To Console    Third color is: ${colors}[2]
