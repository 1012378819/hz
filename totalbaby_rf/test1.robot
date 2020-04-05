*** Settings ***
Documentation    Suite description

*** Test Cases ***
TestRF

    ${a}    set variable  abc
    should not be equal    2+3    5
    should be equal as strings    ${a}    abc
    should not be empty    aa
    should be true    4==4
    should contain    abcd123432    d12
    should end with    hello    lo
    should start with    hello    hel

    ${var}    set variable if    'aa'<>5    9
    log    ${var}

    :for    ${in}    in range    5
    /    log    ${in}

    ${num}    evaluate    random.randint(0,100)    random
    log    ${num}