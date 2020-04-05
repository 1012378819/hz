*** Settings ***
Library  RequestsLibrary
Library  collections
Library  Selenium2Library
*** Test Cases ***
TestGET
    [Tags]    get

    Capture Page Screenshot
    create session    api    http://www.baidu.com
    ${a}    get request    api    /
    should be equal as strings    ${a.status_code}    200
    log    ${a.content}

#    ${responsedata}    to json    ${a.content}
#    ${keys}    Get dictionary keys    ${responsedata}
#    ${items}    Get dictionary Items    ${responsedata}
#    ${values}    Get dictionary Values    ${responsedata}
#    ${str}    Get from dictionary    ${responsedata}
#    log    ${keys}
    log    111222
    delete all sessions
