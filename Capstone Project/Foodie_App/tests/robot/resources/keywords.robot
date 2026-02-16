*** Settings ***
Library     RequestsLibrary
Resource    variables.robot

*** Keywords ***

Create API Session
    Create Session    ${SESSION}    ${BASE_URL}

Create Restaurant
    [Arguments]     ${payload}
    ${response}=    POST On Session    ${SESSION}    /api/v1/restaurants    json=${payload}
    RETURN          ${response}

Create User
    [Arguments]     ${payload}
    ${response}=    POST On Session    ${SESSION}    /api/v1/users/register    json=${payload}
    RETURN          ${response}

Add Dish
    [Arguments]     ${restaurant_id}    ${payload}
    ${endpoint}=    Set Variable        /api/v1/restaurants/${restaurant_id}/dishes
    ${response}=    POST On Session     ${SESSION}                                     ${endpoint}    json=${payload}
    RETURN          ${response}

Place Order
    [Arguments]     ${payload}
    ${response}=    POST On Session    ${SESSION}    /api/v1/orders    json=${payload}
    RETURN          ${response}
