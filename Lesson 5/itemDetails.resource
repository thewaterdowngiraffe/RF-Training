*** Settings ***
Documentation    Grabbing the shopping list items details from Amazon and ebay
Library     itemDetailsfunc.py
Library    QWeb
Library    RPA.Tables
Library    RPA.Excel.Files
Library    String
Library    collections
Variables    itemDetailsfunc.py


*** Variables ***
# ${EXCEL_PATH}=   Lesson 5/shopping_list.csv
# ${SHEET_NAME}    Sheet1

${website_amazon}=     https://www.amazon.ca
${SEARCH_TYPETEXT_AM}    Search Amazon.ca
${FRIST_RESULT_AM}    //*[@class\="a-link-normal _c2Itd_link_pJ4S_ _c2Itd_hidden_9Hszh _c2Itd_outlineOverride_3oVUy"]
${PRODUCT_TITLE_AM}    //span[@id\="productTitle"]
${PRODUCT_RATING_AM}    //span[@class\="a-icon-alt"]
${website_newegg}    https://www.newegg.ca/
${SEARCH_TYPETEXT_NE}    //*[@title\="Search Site"]
${FRIST_RESULT_NE}     //*[@class\="item-title"]
${PRODUCT_TITLE_NE}    //*[@class\="product-title"]
${PRODUCT_REVIEW_NE}    //div[@data-nav\="Reviews"]
${PRODUCT_RATING_NE}    //span[@class\="rating-views-num"]
${PRODUCT_SHIPPINGCOST_AM}     //span[@data-csa-c-type\="element"]
${PRODUCT_SHIPPINGCOST_NE}    //span//strong[contains(text(),'$')]
${skip}    0
${PRODUCT_BRAND_AM}    //div[@id\="productOverview_feature_div"]//div//tr[3]//td[2]
${PRODUCT_SPCE_NE}    //div[@data-nav\="Specs"]
${PRODUCT_BRAND_NE}   //div[@class\="tab-pane"]//table[2]//td
${DELIVERY_DATE_AM}    //span[@class\="a-text-bold"]

*** Keywords ***
Get details from Amazon
    [Documentation]  Unding the keyword and getting details
    [Arguments]    ${item_to_search}
    OpenBrowser    ${website_amazon}     chrome
    TypeText       ${SEARCH_TYPETEXT_AM}    ${item_to_search}\n
    ClickElement   ${FRIST_RESULT_AM}
    ${product}    Create Item    item_to_search=${item_to_search}
    ${product_name}    Get Text    ${PRODUCT_TITLE_AM}
    Set Product Name    product=${product}    value=${product_name} 
    Set Website Name    product=${product}     value=Amazon
    
   ${product_price}    Get Text    $ 
    Set Product Price    product=${product}    value=${product_price}

    ${product_shippingcost}    Get Text    ${PRODUCT_SHIPPINGCOST_AM}
    Set Product Shippingcost    product=${product}    value=${product_shippingcost}
    ${product_brand}    Get Text    ${PRODUCT_BRAND_AM}
    Set Product Brand    product=${product}    value=${product_brand}
    ${delivery_date}    Get Text    ${DELIVERY_DATE_AM}    
    Set Date Of Delivery    product=${product}     value=${delivery_date}
    



    ${status}=    Run Keyword And Return Status    Get Text    ${PRODUCT_RATING_AM}    timeout=3s
    IF    ${status}==True
            ${product_rating}    Get Text    ${PRODUCT_RATING_AM}
            Set Product Rating   product=${product}    value=${product_rating}
    ELSE
            Log To Console     ${skip}
    END
    Close Browser  
    RETURN   ${product}




Get details from NewEgg
    [Documentation] 
    [Arguments]    ${item_to_search}
    OpenBrowser    ${website_newegg}     chrome
    TypeText       ${SEARCH_TYPETEXT_NE}     ${item_to_search}\n
    ClickElement   ${FRIST_RESULT_NE}
    ${product}    Create Item    item_to_search=${item_to_search}
    
    ${product_name}    Get Text    ${PRODUCT_TITLE_NE}
    Set Product Name    product=${product}    value=${product_name}
    Set Website Name    product=${product}     value=Newegg
    
    ${product_price}    Get Text    $ 
    Set Product Price    product=${product}    value=${product_price}

    Click Element    ${PRODUCT_SPCE_NE}
    ${product_brand}    Get Text    ${PRODUCT_BRAND_NE}
    Set Product Brand    product=${product}    value=${product_brand}


    ${status}=    Run Keyword And Return Status    Get Text    ${PRODUCT_SHIPPINGCOST_NE}    timeout=10s
    IF    ${status}==True
        ${product_shippingcost}    Get Text    ${PRODUCT_SHIPPINGCOST_NE}
        Set Product Shippingcost    product=${product}    value=${product_shippingcost}
    ELSE
        Set Product Shippingcost    product=${product}    value=${skip}
    END
    
    ClickElement    ${PRODUCT_REVIEW_NE}
    ${status}=    Run Keyword And Return Status    Get Text    ${PRODUCT_RATING_NE}    timeout=10s
    IF    ${status}==True
        ${product_rating}    Get Text    ${PRODUCT_RATING_NE}
        Set Product Rating   product=${product}    value=${product_rating}
    ELSE
        Set Product Rating   product=${product}    value=${skip}
        Log To Console    ${skip}
    END
    
    Close Browser
    RETURN     ${product}




    

