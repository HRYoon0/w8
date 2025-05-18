from pyhwpx import Hwp
hwpx = Hwp()
hwpx.register_module(
    "FilePathCheckDLL",
    "HwpAutomationModule")

hwpx.open("test2.hwp")
hwpx.Run("SelectAll")
hwpx.Run("ParagraphShapeAlignCenter")
hwpx.save_as("test2_by_macro.hwp")
hwpx.Quit()