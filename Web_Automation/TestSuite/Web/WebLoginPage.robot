*** Settings ***
Resource    ../../Res/Web/GenericFunction.robot
Resource    ../../Res/Web/Login_Functionality.robot
Variables  ../../VariableFiles/Web/Config.py
*** Test Cases ***
#T-1: Verify elements are prsent on Livmore webpage or not
#    Test Setup
#    Verify Title, Logo And Other Links
#    Close Browser
#T-2: Verify Login Fields and Button
#    Test Setup
#    Verify Input Fields, Show Password And Login Button
#    Verify Show Password
#    Close Browser
T-3: Check Login Fuctionality with Username(Invaid) and Password(Valid)
    Test Setup
    Login To Livmor Portal    username=${login_patient_username_invalid}    password=${login_patient_password_valid}
    Validate Error Message And Page URL On Entering Wrong Credentials
    Close Browser
#T-4: Check Login Fuctionality with Username(Valid) and Password(Invalid)
#    Test Setup
#    Login To Livmor Portal    username=${login_patient_username_invalid}    password=${login_patient_password_valid}
#    Validate Error Message And Page URL On Entering Wrong Credentials
#    Close Browser
#T-5: Check Login Fuctionality with Username(Valid) and Password(Invalid)
#    Test Setup
#    Login To Livmor Portal    username=${login_patient_username_invalid}    password=${login_patient_password_valid}
#    Validate Error Message And Page URL On Entering Wrong Credentials
#    Close Browser
#T-6: Check Login Fuctionality with Username(Blank) and Password(Valid)
#    Test Setup
#    Enter Password    password=${login_patient_password_valid}
#    Validate Error message when Username is not entered
#    Close Browser
#T-7: Check Login Fuctionality with Username(Valid) and Password(Blank)
#    Test Setup
#    Enter Username    password=${login_patient_username_valid}
#    Validate Error message when Password is not entered
#    Close Browser
#T-8: After Successful Login Redirecting to correct Page
#    Test Setup
#    Login To Livmor Portal    username=${login_patient_username_valid}    password=${login_patient_password_valid}
#    Close Browser