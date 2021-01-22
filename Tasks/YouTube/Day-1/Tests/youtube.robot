*** Settings ***
Library    ../YouTube/libs/Mobile.py
Library    ../YouTube/libs/Image_Comapre/img_comp.py
*** Variables ***
${img1}     video-1.png
${img2}     video-2.png
${command}    adb shell am start -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity
*** Test Cases ***
T1: Open Youtube and play a video
    Play A Video    ${command}    real madrid    269    730
T2:Screenshot should not be same
   Verify Video    img3=${img1}      img5=${img2}

*** Keywords ***
Play a video
    [Arguments]    ${cmd}    ${search_value}    ${cordinate-1}  ${cordinate-2}
    Execute Adb Shell Command    ${cmd}
    press search
    execute adb shell command    input text    ${search_value}
    Press Enter
    click at coordinates    ${cordinate-1}  ${cordinate-2}
Verify Video
    [Arguments]    ${img3}      ${img5}
    ${result}=    Image Compare   ${img3}      ${img5}





