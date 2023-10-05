import sys


def print_py_ver(actual_version):
    """ Printing to console version of installed and running Python interpreter. """
    print(f'You python ver is, {actual_version}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv
    if args is not None and "-h" in args:
        print("All the help, you need.")
        print("Arguments\t | Description")
        print("-h\t | Presents help")
        sys.exit(0)
        
    PY_VER = sys.version
    print_py_ver(PY_VER)
