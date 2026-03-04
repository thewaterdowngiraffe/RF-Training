*** Settings ***
Documentation    This is the solution doc for lesson 5.
Metadata    Author    Keegan Andrus
Library    QWeb
Library    data.py
Test Setup        OpenBrowser    https://www.amazon.ca    chrome
Test Teardown     Close Browser
Test Template    Search Amazon For Item


*** Test Cases ***
TEMPLATE Sale
    [Documentation]    This uses the template functionailty
    ...    all that needs to happen is i declare the variables
    ...    for the template function.
    ...    Expect a sale
    Logitech MX Vertical Wireless    ${True}

TEMPLATE No Sale
    [Documentation]    This uses the template functionailty
    ...    all that needs to happen is i declare the variables
    ...    for the template function.
    ...    Expect no sale
    DDR5    ${False}


*** Keywords ***
Search For ${Item} On Amazon
    [Documentation]    within amazon searces for `Item`
    ...    and validates that it was searched
    Type Text    Search Amazon.ca    ${Item}
    Press Key    ${EMPTY}    \n
    Verify Text    results for "${Item}"
    ${Product}=    Create Item    ${Item}
    RETURN    ${Product}

Select First Item
    [Documentation]    this just clicks the first search result
    Click Element    xpath=(//*[@tabindex="-1"]/*/*[@src])[1]

Get Price
    [Documentation]    gets the price
    [Arguments]    ${Product}=${NONE}
    ${Price}=    Get Text    $
    IF    '''${Product}''' != '${None}'    Set Price    ${Product}    ${Price}
    RETURN    ${Price}

Get Rating
    [Documentation]    gets the rating
    [Arguments]    ${Product}=${NONE}
    ${Rating}=    Get Text    out of 5    from_start=3
    IF    '''${Product}''' != '${None}'    Set Rating    ${Product}    ${Rating}
    RETURN    ${Rating}

Get Link
    [Documentation]    gets the link
    [Arguments]    ${Product}=${NONE}
    ${Url}=    QWeb.Get Url
    IF    '''${Product}''' != '${None}'    Set Link    ${Product}    ${Url}
    RETURN    ${Url}

Get Details
    [Documentation]    This collects all of the details of the Product
    [Arguments]    ${Product}=${NONE}
    Get Price    ${Product}
    Get Rating    ${Product}
    Get Link    ${Product}

Is Item On Sale
    [Documentation]    returns true it the item is on sale
    ...    and false it not
    [Arguments]    ${Product}=${NONE}
    ${Count}=    Get Element Count    //span[contains(@class,"reinventPriceSavingsPercentageMargin")]
    Log    ${Count}
    IF    ${{'''${Product}''' != 'None'}}    Set Sale    ${Product}    ${{${Count} != 0}}
    RETURN    ${{${Count} != 0}}

Search Amazon For Item
    [Documentation]    this takes in `Item` and searches for it
    ...    then it confirms that it is or is not on sale based on
    ...    if `Expect Sale` is true or false.
    [Arguments]    ${Item}    ${Expect Sale}
    Set Tags    sale:${Expect Sale}    Template
    ${Product}=    Search For ${Item} On Amazon
    Select First Item
    Get Details      ${Product}
    ${is on sale}=    Is Item On Sale
    Should Be Equal    ${is on sale}    ${Expect Sale}
    Log    ${Product}

# Amazon With Keywords Expect Full Price
#     [Documentation]    this uses the Testcase setup and the test
#     ...    case teardown to setup and close the browser.
#     ...    searches for "DDR5" and validate that it is not on sale
#     [Tags]    sale:False    regular format
#     [Template]    NONE
#     ${Product}    Search For DDR5 On Amazon
#     Select First Item
#     Get Details      ${Product}
#     ${is on sale}=    Is Item On Sale    ${Product}
#     Should Not Be True    ${is on sale}
#     Log    ${Product}

# Amazon With Keywords Expect Sale
#     [Documentation]    this uses the Testcase setup and the test
#     ...    case teardown to setup and close the browser.
#     ...    searches for "Logitech MX Vertical Wireless" and validate that it is on sale
#     [Template]    NONE
#     [Tags]    sale:True    regular format
#     ${Product}    Search For Logitech MX Vertical Wireless On Amazon
#     Select First Item
#     Get Details      ${Product}
#     ${is on sale}=    Is Item On Sale
#     Should Be True    ${is on sale}
#     Log    ${Product}
