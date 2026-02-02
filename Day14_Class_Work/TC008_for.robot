*** Test Cases ***
Print Names using for loop
    FOR    ${name}    IN    Bhagya Sanvi Soumya
        Log To Console    ${name}
    END

Print Names using while loop
    ${count}=       Set Variable     1
    WHILE    ${count}<=5
        Log To Console    ${count}
        ${count}=   Evaluate    ${count} + 1
    END
