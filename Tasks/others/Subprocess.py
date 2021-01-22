import subprocess
subprocess.run('adb devices', shell=True)
subprocess.run('adb shell input keyevent 26', shell=True)
subprocess.run('adb shell input swipe 528 2171 528 226', shell=True)
subprocess.run('adb shell input text 1909 &&adb shell input keyevent 66', shell=True)
subprocess.run('adb shell screencap -p /sdcard/screencap-subprocess.png && adb pull /sdcard/screencap-subprocess.png', shell=True)
subprocess.run('adb shell screenrecord /sdcard/demo-subprocess.mp4 && adb pull /sdcard/demo-subprocess.mp4', shell=True)
