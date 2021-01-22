import cv2
from uiautomator import Device
from uiautomator import device as d
import time


def image_compare(img1, img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    difference = cv2.subtract(img2, img1)
    r, b, g = cv2.split(difference)
    if cv2.countNonZero(r) != 0 or cv2.countNonZero(r) != 0 or cv2.countNonZero(r) != 0:
        print("Video is Playing as images are not Equal")
        return True
    else:
        print("Video is paused or not playing as images are equal")
        return False


def take_screenshots():
    d.screenshot('yt1.png')
    time.sleep(5)
    d.screenshot('yt2.png')


