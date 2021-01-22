*** Settings ***
Library    SeleniumLibrary
Variables  ../../VariableFiles/Web/Config.py
*** Keywords ***
Login to Livmor Portal
    [Arguments]    ${username}    ${password}
    Wait Until Page Contains Element    ${login_page_username_field}    timeout=15 seconds    error=Element not present
    Enter Username  ${username}
    Enter Password  ${password}
    Click Element    ${login_page_login_button}
Enter Username
    [Arguments]    ${username}
    Wait Until Page Contains Element    ${login_page_username_field}    timeout=15 seconds    error=username field not present
    Click Element    ${login_page_username_field}
    Input Text    ${login_page_username_field}    ${username}
    Click Element    ${login_page_login_button}
Enter Password
    [Arguments]    ${password}
    Wait Until Page Contains Element    ${login_page_password_field}    timeout=15 seconds    error=password field not present
    Click Element    ${login_page_password_field}
    Input Password    ${login_page_password_field}    ${password}
    Click Element    ${login_page_login_button}
Validate Page URL with wrong or blank credentials
    ${return_url}    Get Location
    Should Be Equal    ${return_url}    ${login_error_url}
Validate Error Message and Page URL on entering Wrong Credentials
    Wait Until Page Contains Element    ${login_error_message_locator}  timeout=15 seconds    error=Page still loading
    Validate Page URL With Wrong Or Blank Credentials
    ${return_error_message}    Get Text    ${login_error_message_locator}
    Should Be Equal    ${return_error_message}    ${login_error_message}
Validate Error message when Username is not entered
    Wait Until Page Contains Element  ${login_error_blank_username_locator}    timeout=15 seconds    error=username msg not visible
    ${return_uname_message}    Get Text    ${login_error_blank_username_locator}
    Should Be Equal    ${return_uname_message}    ${login_error_blank_username}
Validate Error message when Password is not entered
    Wait Until Page Contains Element  ${login_error_blank_password_locator}    timeout=15 seconds    error=pass msg not visible
    ${return_pass_message}    Get Text    ${login_error_blank_password_locator}
    Should Be Equal    ${return_pass_message}    ${login_error_blank_password}