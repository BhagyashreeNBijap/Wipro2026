*** Settings ***
Library    OperatingSystem
*** Test Cases ***
#1)IF condition (basic)
 IF Condition Example
    ${age}=     Set Variable    20
    IF    ${age} >= 18
        Log  Eligible to vote
        END

#2)IF ELSE:
IF ELSE Example
    ${num}=     Set Variable    5
    IF    ${num} > 10
        Log  Greater than 10
    ELSE
        Log  Less than ot equal to 10
    END

#3)IF-ELSE IF – ELSE
IF ELSE IF Example
    ${marks}=   Set Variable    75
    IF  ${marks} >= 90
        Log  Grade A
    ELSE IF  ${marks} >= 75
        Log  Grade B
    ELSE
        Log  Grade C
    END

#4)Inline IF (short condition)
Inline IF Example
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'    Log    Test Passed

#5)FOR loop (basic list)

FOR Loop Basic
    FOR    ${item}    IN    one    two    three
        Log    Item: ${item}
    END


#6)FOR loop with list variable
*** Variables ***
@{COLORS}    Red    Green    Blue

*** Test Cases ***
FOR Loop With List
    FOR    ${color}    IN    @{COLORS}
        Log    Color: ${color}
    END

#7)For loop - in range
FOR Loop Range
    FOR    ${i}    IN RANGE    1    6
        Log    Number: ${i}
    END

#8)FOR loop – with step
FOR Loop With Step
    FOR    ${i}    IN RANGE    0    10    2
        Log    Value: ${i}
    END

#️9)FOR loop – ENUMERATE
FOR Loop Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log    ${index} = ${value}
    END

#10)For loop = ZIP(multiple lists
FOR using zip
    @{Users}=    Create List    admin    user
    @{Pwds}=     Create List    admin123    user123

    @{pairs}=    Evaluate    list(zip($Users, $Pwds))

    FOR    ${pair}    IN    @{pairs}
        Log To Console    ${pair}[0] / ${pair}[1]
    END


#11)Nested FOR loop
Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log    i=${i}, j=${j}
        END
    END

#12)For  loop with IF condition
FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log    Found 3
        END
    END

#13)BREAk (exit loop)
BREAK Example
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log    ${i}
    END

#14)CONTINUE (skip iteration)
CONTINUE Example
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log    ${i}
    END

#15)WHILE loop (Robot Framework 4+)
WHILE Loop Example
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END

#16)WHILE with BREAk
WHILE Loop With BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log    ${i}
        ${i}=    Evaluate    ${i} + 1
    END

#17)ERROR HANDLING (Control Structure)
#TRY/EXCEPT/FINALLY
Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log    Error handled
    FINALLY
        Log    Always executed
    END






