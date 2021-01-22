from time import sleep

from uiautomator import Device
from uiautomator import device as d
import string


def play_pause_toggle():
    button_dict = {}
    button_dict = d(resourceId='com.google.android.youtube:id/player_control_play_pause_replay_button').info
    if button_dict['contentDescription'] == 'Play video':
        d(resourceId='com.google.android.youtube:id/player_control_play_pause_replay_button').click()
        return "Now playing video"
    else:
        d(resourceId='com.google.android.youtube:id/player_control_play_pause_replay_button').click()
        return 'Video paused'


def next_video():
    d(description='Next video').click()
    return 'Playing next video'


def previous_video():
    button_status = {}
    button_status = d(description='Previous video').info
    if not button_status['enabled']:
        return 'Previous button is disabled'
    else:
        d(description='Previous video').click()
        return 'Playing previous video'


def seek_bar():
    video_position = {}
    video_position = d(className='android.widget.SeekBar').info
    return video_position['contentDescription']


def video_details():
    video_length = {}
    current_time = {}
    video_title = {}
    current_time = d(resourceId='com.google.android.youtube:id/time_bar_current_time').info
    video_length = d(resourceId='com.google.android.youtube:id/time_bar_total_time').info
    video_title = d(resourceId='com.google.android.youtube:id/title').info
    s = video_length['text']
    s = s.replace('/ ', '')
    print("Title of video is " + video_title['text'])
    print("Total length of video is : " + s)
    print("Current position of video is : " + current_time['text'])


print(previous_video())
