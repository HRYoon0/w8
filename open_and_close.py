from pyhwpx import Hwp
import time

hwpx = Hwp(new=True, visible=True)
time.sleep(2)
hwpx.Quit()