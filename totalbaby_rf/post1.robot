*** Settings ***
Library  RequestsLibrary

*** Test Cases ***
TestPost
    [Tags]    post

    ${requestheader}    create dictionary    Content-type=application/x-www-form-urlencoded       Accept-Encoding=gzip,deflate      X-device-id=5715c06e5e904e934f6ccf13    User-Agent=BTComplete/4.5.4
    create session    url    http://192.168.199.43:3002    ${requestheader}
    ${requestbody}    create dictionary    username=mm@test.com    password=111111     app_version=4.5.4       ios_version=9.3    device_model=iPhone Simulator
    ${addr}    post request    url    v1/api/u/user/login    data=${requestbody}
    log    ${addr.status_code}
    log    ${addr.content}
    log    ${addr.json()}