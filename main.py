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

mouse = (1555, 2217) # 스크린 x, y 좌표


def click_video():
    print(f'{datetime.now().strftime("%H:%M:%S")} 비디오 ON/OFF 클릭 완료')
    (x, y) = mouse
    pyautogui.moveTo(x, y)
    pyautogui.click()


def pending():
    schedule.run_pending()
    time.sleep(1)

def test():
    pass


if __name__ == '__main__':
    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
    print('실행되었습니다. 🐯')
    schedule.every().hour.at(f'50:{get_secs()}').do(click_video)
    schedule.every().hour.at(f'00:{get_secs()}').do(click_video)

    while True:
        dt = datetime.now()
        h = dt.hour
        if h == 12 or h == 8 or h >= 17:
            time.sleep(10)
            continue
        pending()
