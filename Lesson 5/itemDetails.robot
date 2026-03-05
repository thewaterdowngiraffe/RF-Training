*** Settings ***
Documentation    Grabbing the shopping list items details from Amazon and ebay
Metadata    Moumita D.
Resource    itemDetails.resource
Library    itemDetailsfunc.py
Library    RPA.Tables
Library    collections



*** Test Cases ***
Search and get item details from website
    [Documentation]    Read item from excel
    [Setup]    Clear Csv
    ${csv_data}=    Read table from CSV    path=Lesson 5/shopping_list.csv    delimiters=;

    FOR    ${item}    IN    @{csv_data}
        
        ${product_am}    Get details from Amazon   ${item}[Name]
       
        ${product_ne}    Get details from NewEgg    ${item}[Name]
       
        Find Cheapest    dictForam=${product_am}   dictForne=${product_ne}
        


    
    END
        



    