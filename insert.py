from pyhwpx import Hwp
hwpx = Hwp()
hwpx.register_module(
    "FilePathCheckDLL",
    "HwpAutomationModule")

hwpx.insert_text("Hello G-DEAL")
hwpx.save_as("hello.hwp")
hwpx.Quit()