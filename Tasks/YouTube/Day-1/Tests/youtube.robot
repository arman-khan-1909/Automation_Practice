*** Settings ***
Library    ../libs/Image_Comapre/Mobile.py
Library    ../libs/Image_Comapre/img_comp.py
*** Variables ***
${img1}     video-1.png
${img2}     video-2.png
${command}    am start -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity
${msg}    Screenshots are not equal, video is playing
*** Test Cases ***
T1: Open Youtube and play a video
    Play A Video    ${command}  269    730
T2:Screenshot should not be same
   Verify Video    ${img1}    ${img2}

*** Keywords ***
Play a video
    [Arguments]    ${cmd}    ${cordinate-1}    ${cordinate-2}
    Execute Adb Shell Command    ${cmd}
    press search
    Execute adb shell command    input text real madrid
    Press Enter
    click at coordinates    ${cordinate-1}    ${cordinate-2}
Verify Video
    [Arguments]    ${img3}    ${img5}
    ${result}=    Image Compare    ${img3}    ${img5}
    Should Be True    ${result}==True




