*** Settings ***
Library    ../calculator.py    AS    CALC

*** Test Cases ***
Validate Subtraction
    FOR    ${A}     IN RANGE    -10    10
        FOR    ${B}    IN RANGE    -10    10
            ${result}=    CALC.Subtract    ${A}    ${B}
            Should Be Equal    ${result}    ${{${A}-${B}}}    Subtract failed
        END
    END


Validate Addition
    FOR    ${A}     IN RANGE    -10    10
        FOR    ${B}    IN RANGE    -10    10
            ${result}=    CALC.add    ${A}    ${B}
            Should Be Equal    ${result}    ${{${A}+${B}}}    addition failed
        END
    END


Validate multiply
    FOR    ${A}     IN RANGE    -10    10
        FOR    ${B}    IN RANGE    -10    10
            ${result}=    CALC.multiply    ${A}    ${B}
            Should Be Equal    ${result}    ${{${A}*${B}}}    multiplication failed
        END
    END

Validate exponent POS
    FOR    ${A}     IN RANGE    0    10  0.5
        FOR    ${B}    IN RANGE    0    10
            ${result}=    CALC.exponent    ${A}    ${B}
            Should Be Equal    ${result}    ${{${A}**${B}}}    exponent failed
        END
    END

Validate exponent neg
    FOR    ${A}     IN RANGE    -5    1
        FOR    ${B}    IN RANGE    -5    1
            Log To Console    ${A}^${B}=${{(${A})**(${B})}}
            ${result}=    CALC.exponent    ${A}    ${B}
            Should Be Equal    ${result}    ${{(${A})**(${B})}}    exponent failed
        END
    END

Validate exponent Float
    FOR    ${A}     IN RANGE    1    10
        FOR    ${B}    IN RANGE    1    5    0.5
            ${result}=    CALC.exponent    ${A}    ${B}

            Should Be Equal    ${result}    ${{(${A})**(${B})}}    exponent failed
        END
    END


Validate sqrt
    FOR    ${A}     IN RANGE    0    1000
        ${result}=    CALC.sqrt    ${{${A}*${A}}}
        Should Be Equal    ${result}    ${A}    sqrt failed
    END


