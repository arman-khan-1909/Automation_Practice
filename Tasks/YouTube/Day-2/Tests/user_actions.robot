*** Settings ***
Library    ../libs/Mobile.py
Library    ../libs/user_actions.py
*** Variables ***
*** Test Cases ***
T1: Is Video playing or not
    Check Video Status
T2: Check video details
    Print Details
*** Keywords ***
Check Video Status
    ${result}=    Play Pause Toggle
    Log    ${result}
Print Details
    Video Details
