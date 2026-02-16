*** Settings ***
Resource    resources/keywords.robot
Library     Collections
Suite Setup     Create API Session

*** Test Cases ***
Complete Order Flow

    # Create Restaurant
    ${restaurant}=    Create Dictionary
    ...    name=FlowResto
    ...    category=Indian
    ...    location=Hyderabad
    ...    contact=9999999999

    ${rest_response}=    Create Restaurant    ${restaurant}
    Status Should Be    201    ${rest_response}

    ${rest_body}=    Set Variable    ${rest_response.json()}
    ${rest_id}=    Get From Dictionary    ${rest_body}    id


    # Add Dish
    ${dish}=    Create Dictionary
    ...    name=Biryani
    ...    type=Veg
    ...    price=400
    ...    available_time=12:00
    ...    image=b.jpg

    ${dish_response}=    Add Dish    ${rest_id}    ${dish}
    Status Should Be    201    ${dish_response}

    ${dish_body}=    Set Variable    ${dish_response.json()}
    ${dish_id}=    Get From Dictionary    ${dish_body}    id


    # Create User
    ${user}=    Create Dictionary
    ...    name=FlowUser
    ...    email=flow@test.com
    ...    password=password123

    ${user_response}=    Create User    ${user}
    Status Should Be    201    ${user_response}

    ${user_body}=    Set Variable    ${user_response.json()}
    ${user_id}=    Get From Dictionary    ${user_body}    id


    # Create Dish List (IMPORTANT FIX)
    ${dish_list}=    Create List    ${dish_id}

    # Create Order Payload
    ${order_payload}=    Create Dictionary
    ...    user_id=${user_id}
    ...    restaurant_id=${rest_id}
    ...    dishes=${dish_list}

    ${order_response}=    Place Order    ${order_payload}
    Status Should Be    201    ${order_response}
