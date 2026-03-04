*** Settings ***
Documentation    This is the solution doc for lesson 5.
Metadata    Author    Keegan Andrus
Resource    amazon.resource
Test Setup        OpenBrowser    https://www.amazon.ca    chrome
Test Teardown     Close Browser


*** Test Cases ***
Item Is On Sale
    [Documentation]    This uses the template functionailty
    ...    all that needs to happen is i declare the variables
    ...    for the template function.
    ...    Expect a sale
    ${Product}=   Search For Logitech MX Vertical Wireless On Amazon
    Select First Item
    Get Details    ${Product}
    ${is on sale}=    Is Item On Sale
    Should Be Equal    ${is on sale}    ${True}
    Log    ${Product}

Item Is Not On Sale
    [Documentation]    This uses the template functionailty
    ...    all that needs to happen is i declare the variables
    ...    for the template function.
    ...    Expect no sale
    ${Product}=    Search For DDR5 On Amazon
    Select First Item
    Get Details      ${Product}
    ${is on sale}=    Is Item On Sale
    Should Be Equal    ${is on sale}    ${False}
    Log    ${Product}
