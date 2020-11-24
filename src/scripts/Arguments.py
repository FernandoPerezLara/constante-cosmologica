import argparse

# This function parses all the arguments
def readArguments():
    parser = argparse.ArgumentParser(description="Program dedicated to the study of the origin of the cosmological constant.")

    parser.add_argument("--dont-save", action="store_true", dest="dontSave", default=False, help="Results are not saved, they are only displayed")

    return (parser.parse_args())