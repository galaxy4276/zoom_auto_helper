import pyautogui
import schedule
import os
import pyscreeze
import PIL
import time
from time_utils import get_secs


__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

current_dir = os.getcwd()
video_on_img = os.path.join(current_dir, 'video_on.png')


def click_video():
    pyautogui.moveTo(138, 1286)
    pyautogui.click()


if __name__ == '__main__':
    schedule.every().hour.at(f':50:${get_secs()}').do(click_video)
    schedule.every().hour.at(f':00:{get_secs()}').do(click_video)
    print(f'video_on_img: {video_on_img}')

    while True:
        schedule.run_pending()
        time.sleep(1)