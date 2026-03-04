*** Settings ***
Library    data.py
Library    QWeb
Documentation    this file allows for site scraping on amazon or newegg.
...    all data is logged to a data object.


*** Keywords ***
Search For ${Item} On ${site}
    [Documentation]    within Amazon or newegg searces for `Item`
    ...    and validates that it was searched
    IF    '${site}' == 'Amazon'
        Type Text    Search Amazon.ca    ${Item}\n
        Verify Text    results for "${Item}"
    ELSE IF    '${site}' == 'Newegg'
        Type Text    Search    ${Item}\n
        Verify Text    Search Results: "${Item}"
    END
    ${Product}=    Create Item    ${Item}
    RETURN    ${Product}

Select First Item
    [Documentation]    this just clicks the first search result based on the ${site}
    [Arguments]    ${site}=Amazon
    IF    '${site}' == 'Amazon'
        Click Element    xpath=(//*[@tabindex="-1"]/*/*[@src])[1]
    ELSE IF    '${site}' == 'Newegg'
        Click Element    xpath=//*[contains(@class,"item-cell")]//a[@class="item-img"]
    END

Get Price
    [Documentation]    gets the price
    [Arguments]    ${Product}=${NONE}
    ${Price}=    Get Text    $
    IF    '''${Product}''' != '${None}'    Set Price    item=${Product}    value=${Price}
    RETURN    ${Price}

Get Rating
    [Documentation]    gets the rating
    [Arguments]    ${Product}=${NONE}    ${site}=Amazon
    IF    '${site}' == 'Amazon'
        ${Rating}=    Get Text    out of 5    from_start=3
    ELSE IF    '${site}' == 'Newegg'
        ${Rating}=    Get Attribute    locator=//*[@class="product-rating"]/i    attribute=title
    END
    IF    '''${Product}''' != '${None}'    Set Rating    item=${Product}    value=${Rating}
    RETURN    ${Rating}

Get Arival Date
    [Documentation]    gets the arival date for amazon. defaults to '' for newegg
    [Arguments]    ${Product}=${NONE}    ${site}=Amazon
    IF    '${site}' == 'Amazon'
        ${Arival Date}=    Get Text    locator=//*[@id="deliveryBlockMessage"]//span/span
    ELSE IF    '${site}' == 'Newegg'
        ${Arival Date}=    Set Variable    ${{""}}
    END

    IF    '''${Product}''' != '${None}'    Set Arival Date    item=${Product}    value=${Arival Date}
    RETURN    ${Arival Date}

Get Shipping Fee
    [Documentation]    gets the shipping fee
    [Arguments]    ${Product}=${NONE}    ${site}=Amazon
    IF    '${site}' == 'Amazon'
        ${Shipping Fee}=    Get Text    locator=//*[@id="deliveryBlockMessage"]//span/span/..   between=???delivery
    ELSE IF    '${site}' == 'Newegg'
        ${Shipping Fee}=    Get Text    locator=//ul[@class="price"]//li[@class="price-ship"]/span    between=+ ??? Shipping

        # ${Shipping Fee}=    Set Variable    0
    END
    IF    '''${Product}''' != '${None}'    Set Delivery Cost    item=${Product}    value=${Shipping Fee}
    RETURN    ${Shipping Fee}

Get Rating Count
    [Documentation]    gets the rating count
    [Arguments]    ${Product}=${NONE}    ${site}=Amazon

    IF    '${site}' == 'Amazon'
        ${Rating Count}=    Get Text    locator=//*[@id="acrCustomerReviewText"]    between=(???)    #    from_end=4    from_front=4
    ELSE IF    '${site}' == 'Newegg'
        ${Rating Count}=    Get Text    locator=//*[@data-nav="Reviews"]/span    between=(???)
    END

    IF    '''${Product}''' != '${None}'    Set Rating Count    item=${Product}    value=${Rating Count}
    RETURN    ${Rating Count}

Get Link
    [Documentation]    gets the link
    [Arguments]    ${Product}=${NONE}
    ${Url}=    QWeb.Get Url
    IF    '''${Product}''' != '${None}'    Set Link    ${Product}    ${Url}
    RETURN    ${Url}

Get Details
    [Documentation]    This collects all of the details of the Product
    [Arguments]    ${Product}=${NONE}    ${site}=Amazon
    Get Price    ${Product}
    Get Rating    ${Product}    ${site}
    Get Link    ${Product}
    Get Rating Count    ${Product}    ${site}
    Get Arival Date    ${Product}    ${site}
    Get Shipping Fee    ${Product}    ${site}

Is Item On Sale
    [Documentation]    returns true it the item is on sale and updates the object
    ...    and false it not
    [Arguments]    ${Product}=${NONE}
    ${is present}=    Is Element    //span[contains(@class,"reinventPriceSavingsPercentageMargin")]
    IF    ${{'''${Product}''' != 'None'}}    Set Sale    ${Product}    ${is present}
    RETURN    ${is present}

Get ${site} Detalis
    [Documentation]    gets the details for amazon or newegg depending on
    ...    the `site` details. returns the object with all details.
    [Arguments]    ${item}
    OpenBrowser    https://www.${site}.ca    chrome    # -headless
    ${Product}=    Search For ${item} On ${site}
    Select First Item    ${site}
    Get Details      ${Product}    ${site}
    [Teardown]    Close Browser
    RETURN    ${Product}
