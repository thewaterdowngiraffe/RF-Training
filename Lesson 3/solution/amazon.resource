*** Settings ***
Library    data.py
Library    QWeb
Documentation    this is the resource file


*** Keywords ***
Search For ${Item} On Amazon
    [Documentation]    within amazon searces for `Item`
    ...    and validates that it was searched
    Type Text    Search Amazon.ca    ${Item}\n
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
    IF    '''${Product}''' != '${None}'    Set Price    item=${Product}    value=${Price}
    RETURN    ${Price}

Get Rating
    [Documentation]    gets the rating
    [Arguments]    ${Product}=${NONE}
    ${Rating}=    Get Text    out of 5    from_start=3
    IF    '''${Product}''' != '${None}'
        Set Rating    item=${Product}
        ...           value=${Rating}
    END
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
