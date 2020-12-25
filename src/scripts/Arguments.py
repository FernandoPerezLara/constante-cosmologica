import argparse

# This function parses all the arguments
def readArguments():
    parser = argparse.ArgumentParser(description="Program dedicated to the study of the origin of the cosmological constant.")

    parser._actions[0].help = "Show this help message and exit"
    parser.add_argument("--dont-save", action="store_true", dest="dontSave", default=False, help="Results are not saved, they are only displayed")
    parser.add_argument("--hide", action="store_true", dest="hide", default=False, help="Results are not displayed on the screen")
    parser.add_argument("--parameters", action="store_true", dest="parameters", default=False, help="Hide entered parameters")

    return (parser.parse_args())