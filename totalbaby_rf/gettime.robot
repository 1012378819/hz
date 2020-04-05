*** Settings ***
Library  RequestsLibrary
Library  collections
*** Test Cases ***
TestGetTime
    [Tags]    DEBUG

#    test
    ${list}    create list    user    passwd    age
    log    ${list}
    :for    ${i}    in    ${list}
    \    log    ${i}
    log    outside loop
    ${dict}    create dictionary    user=mm@test.com    passwd=111111    content-type=lallala
    log    ${dict}
    log    ${dict.user}
    :for    ${i}    in    ${dict}
    \    log    ${i}
    \    log    ${dict[i]}
    log    outside loop



    create session    url    http://192.168.199.43:3002
    ${getResponse}    get request    url    /v2/api/time/get
    should be equal as strings    ${getresponse.status_code}    200
    log    ${getResponse}
    log    ${getResponse.content}
    log    ${getresponse.status_code}
    ${a}    set variable    ${getresponse.content}
    ${toJson}    to json    ${a}
#    :for
#    ${x}    get dictionary keys    ${toJson}
#    ${y}    get dictionary items    ${toJson}
#    ${z}    get dictionary values    ${toJson}
#    log    ${x}
#    log    ${y}
#    log    ${z}
#    ${d}    get from dictionary
    delete all sessions

