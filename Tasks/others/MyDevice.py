from uiautomator import Device
from uiautomator import device as d
from time import sleep
import subprocess
import os


def menuscreen():
    # d.screen.on()
    # d.swipe(360, 1000, 360, 200)
    # subprocess.run('adb shell input text 98273  && adb shell input keyevent 66', shell=True)
    # d.click(367, 1117)
    d(descriptionContains="Apps").click()


def playstore(app):
    try:
        d(className='android.widget.TextView', text='Play Store').click()
        sleep(2)
        d(className='android.widget.TextView', text='Search for apps & games').click()
        sleep(1)
        d(className='android.widget.EditText', text='Search for apps & games').set_text("chrome")
        d.press.enter()
    except Exception as e:
        print(e)


def openapp(name):
    try:
        d(className='android.widget.TextView', text=name.title()).click()
        search = d(className='android.widget.TextView', text='Search for apps & games')
        search.set_text('chrome')
    except Exception as e:
        print(e)


menuscreen()
# open_app('play store')
playstore('chrome')
