*** Settings ***
Metadata    Author    Keegan Andrus
Resource    siteScraping.resource
Library    RPA.Tables
Test Teardown     Close Browser
Documentation    this scrapes data from amazon and newegg.


*** Variables ***
${shopping list}    shopping_list.csv


*** Test Cases ***
Get Cheapest
    [Documentation]    for each item in the csv in the `shopping list` file data will
    ...    be pulled from newegg and amazon. the cheapest will be logged to the data.json file.
    [Setup]    NONE
    ${csv_data}=    Read Table From CSV    path=${shopping list}   delimiters=;
    Write Data    # prep the file
    FOR    ${row}    IN    @{csv_data}
        ${amazon}=    Get Amazon Detalis    item=${row}[name]
        ${newegg}=    Get Newegg Detalis    item=${row}[name]
        ${best}=    Get Best     ${amazon}    ${newegg}
        Log    ${best}
    END
    [Teardown]    NONE
