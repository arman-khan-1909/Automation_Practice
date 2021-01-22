*** Settings ***
Library      ${EXECDIR} /C:/Users/Arman/PycharmProjects/untitled/ContactsScenario/libs/ContactApp.py
#Resource    ${EXECDIR}/ContactsScenario/Generic.robot
#Resource    /ContactsScenario/Generic.robot
Library      ContactsScenario/libs/ContactApp.py
*** Variables ***
${name1}     robot  
${number1}   1234
${email1}    test@gmail.com
#*** Keywords ***
#open contact app
#add contact    ${name}  ${number}   ${email}
*** Test Cases ***
Test1: Contact app shoud launch
   Open Contact List
   Create Contact    name=${name1}    number=${number1}     email=${email1}
#Test2: Contact should be created successfully
#    add_contact    ${name}  ${number}   ${email}
*** Keywords ***
Open Contact List
    open contact app
Create Contact
    [Arguments]    ${name}  ${number}   ${email}​​​​​​​
    add contact   ${name}  ${number}   ${email}
