*** Settings ***


*** Test Cases ***
TestA
    [Tags]    DEBUG

#    log    aaa
#    ${a}    get time
#    log    ${a}

#if
    ${score}    set variable    59
    run keyword if    ${score}>80    log    'you秀'
    ...    ELSE IF    ${score}>60    log    及格
    ...    ELSE    log    不及格


    @{abc}    create list    a    b    c
    :for    ${i}    in    @{abc}
    \    log    ${i}

#    ${abc}    create list    a    b    c
#    :for    ${i}    in    ${abc}
#    \    log    ${i}

    @{abc}    create list    a    b    c
    :for    ${i}    in    @{abc}
    \    exit for loop if    '${i}'=='c'
    log    ${i}

    @{abc}    create list    a    b    c
    :for    ${i}    in    @{abc}
    \    exit for loop if    '${i}'=='c'
    \    log    ${i}

    @{abc}    create list    a    b    c
    :for    ${i}    in    @{abc}
    \    run keyword if    '${i}'=='b'    exit for loop
    \    log    ${i}

    @{abc}    create list    a    b    c
    :for    ${i}    in    @{abc}
    \    run keyword if    '${i}'=='b'    exit for loop
    log    ${i}

*** Test Cases ***
TestB
    ${i}    evaluate    1+3
    log    ${i}

    ${i}    set variable    1+3
    log    ${i}

    ${a}    set variable    random.randint(1,100)    random
    log    ${a}

#没成功
#    ${s}    evaluate    os.system('python  G:/useful/selenium+py/test/a.py')    os
#    log    ${s}