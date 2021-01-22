*** Settings ***
Library    SeleniumLibrary
Variables  ../../VariableFiles/Web/Config.py
*** Keywords ***
Test Setup
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
Verify Title, Logo And Other Links
    Title Should Be    ${login_page_title}
    Scroll Element Into View    ${login_page_privacy}
    Page Should Contain Link    ${login_page_contact_us_link}
    Page Should Contain Element    ${login_page_privacy}
    Page Should Contain Element    ${login_page_tnc}
    Page Should Contain Image   ${login_page_livmor_logo}
Verify Input Fields, Show Password and Login Button
    Element Attribute Value Should Be    ${login_page_username_field}    placeholder    ${login_page_username_field_placeholder}
    Element Attribute Value Should Be    ${login_page_password_field}    placeholder    ${login_page_password_field_placeholder}
    Element Attribute Value Should Be    ${login_page_password_field}   type    ${login_page_password_field_type}
    Page Should Contain Element    ${login_page_login_button}
    Element Attribute Value Should Be    ${login_page_login_button}   type    sumbit
Verify Show Password
    Click Element    ${login_page_show_password}
    Element Attribute Value Should Be    id:${login_page_password_field}   type    ${login_page_password_field_type_clicked_show}




