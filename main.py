import pyautogui
import schedule
import pyscreeze
import PIL
import time
from time_utils import get_secs
from PIL import ImageGrab
from functools import partial
from datetime import datetime

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION


def click_video():
    print(f'{datetime.now().strftime("%H:%M:%S")} 비디오 ON/OFF 클릭 완료')
    pyautogui.moveTo(138, 1286)
    pyautogui.click()


def pending():
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
    dt = datetime.now()
    h = dt.hour
    m = dt.minute
    schedule.every().hour.at(f'50:{get_secs()}').do(click_video)
    schedule.every().hour.at(f'00:{get_secs()}').do(click_video)

    while True:
        if dt.hour == 12:
            time.sleep(1)
            continue
        schedule.run_pending()
        time.sleep(1)
