import sys


def print_py_ver(actual_version):
    print(f'You python ver is, {actual_version}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    py_ver = sys.version
    print_py_ver(py_ver)
