import pyautogui
import schedule
import pyscreeze
import PIL
import time
from time_utils import get_secs
from PIL import ImageGrab
from functools import partial

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION


def click_video():
    pyautogui.moveTo(138, 1286)
    pyautogui.click()


if __name__ == '__main__':
    click_video()
    schedule.every().hour.at(f'50:{get_secs()}').do(click_video)
    schedule.every().hour.at(f'00:{get_secs()}').do(click_video)

    while True:
        schedule.run_pending()
        time.sleep(1)
