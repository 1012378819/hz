*** Settings ***
Library  RequestsLibrary

*** Test Cases ***
TestPost
    [Tags]    post

#    ${dict}    create dictionary  Content-type=application/x-www-form-urlencoded
    ${requestheader}    create dictionary  User-Language=11    language=22    version_code=33    platform=44    Content-type=application/x-www-form-urlencoded    Accept=application/json    charset=utf-8    Accept-Encoding=gzip,deflate    timezone=Asia/Shanghai    X-device-id=5715c06e5e904e934f6ccf13    User-Agent=BTComplete/4.5.4
    create session    url    http://192.168.199.43:3002    ${requestheader}
    ${requestbody}    create dictionary    username=mm@test.com    password=111111    device_owner=AA    device_id=BA8150B3-0606-49DB-8AB0-E4A4F882FFF3    app_version=4.5.4    platform=iOS    timezone=sh    language=en-US    ios_version=9.3    device_model=iPhone Simulator
    ${addr}    post request    url    v1/api/u/user/login    data=${requestbody}
    log    ${addr.status_code}
    log    ${addr.content}
    log    ${addr.json()}
