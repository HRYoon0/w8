from pyhwpx import Hwp
import time

hwpx = Hwp()
hwpx.open("test1.hwp")
time.sleep(5)
hwpx.save_as("test2.hwp")
hwpx.Clear()