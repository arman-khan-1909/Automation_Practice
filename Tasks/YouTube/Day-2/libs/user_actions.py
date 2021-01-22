from uiautomator import Device
from uiautomator import device as d


def play_pause_toggle():
    button_dict = {}
    button_dict = d(resourceId='com.google.android.youtube:id/player_control_play_pause_replay_button').info
    if button_dict['contentDescription'] == 'Play video':
        d(resourceId='com.google.android.youtube:id/player_control_play_pause_replay_button').click()
        return "Now playing video"
    else:
        d(resourceId='com.google.android.youtube:id/player_control_play_pause_replay_button').click()
        return 'Video paused'


def seek_bar():
    video_position = {}
    video_position = d(className='android.widget.SeekBar').info
    return video_position['contentDescription']


play_pause_toggle()


