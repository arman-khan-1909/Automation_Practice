*** Settings ***
Library    MyDevice.py
*** Variables ***
${app_name}     chrome
*** Keywords ***
Search
    playstore      ${app_name}
*** Test Cases ***
Search for app name
    Search