import os
import random
import time
from collections import deque


HIDE_CURSOR = '\x1b[?25l'
GREEN = '\u001b[38;5;46m'
TAIL = '\u001b[38;5;22m'
SECTAIL = '\u001b[38;5;28m'
THRDTAIL = '\u001b[38;5;34m'
THRDHEAD = '\u001b[38;5;47m'
SECHEAD = '\u001b[38;5;77m'
HEAD = '\u001b[38;5;194m'
ENDC = '\033[0m'

# change font size-------------------------------------------------------------------------------------
import sys
from ctypes import POINTER, WinDLL, Structure, sizeof, byref
from ctypes.wintypes import BOOL, SHORT, WCHAR, UINT, ULONG, DWORD, HANDLE


LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11


class COORD(Structure):
    _fields_ = [
        ("X", SHORT),
        ("Y", SHORT),
    ]


class CONSOLE_FONT_INFOEX(Structure):
    _fields_ = [
        ("cbSize", ULONG),
        ("nFont", DWORD),
        ("dwFontSize", COORD),
        ("FontFamily", UINT),
        ("FontWeight", UINT),
        ("FaceName", WCHAR * LF_FACESIZE)
    ]


kernel32_dll = WinDLL("kernel32.dll")

get_last_error_func = kernel32_dll.GetLastError
get_last_error_func.argtypes = []
get_last_error_func.restype = DWORD

get_std_handle_func = kernel32_dll.GetStdHandle
get_std_handle_func.argtypes = [DWORD]
get_std_handle_func.restype = HANDLE

get_current_console_font_ex_func = kernel32_dll.GetCurrentConsoleFontEx
get_current_console_font_ex_func.argtypes = [HANDLE, BOOL, POINTER(CONSOLE_FONT_INFOEX)]
get_current_console_font_ex_func.restype = BOOL

set_current_console_font_ex_func = kernel32_dll.SetCurrentConsoleFontEx
set_current_console_font_ex_func.argtypes = [HANDLE, BOOL, POINTER(CONSOLE_FONT_INFOEX)]
set_current_console_font_ex_func.restype = BOOL


def change_font():
    # Get stdout handle
    stdout = get_std_handle_func(STD_OUTPUT_HANDLE)
    if not stdout:
        print("{:s} error: {:d}".format(get_std_handle_func.__name__, get_last_error_func()))
        return
    # Get current font characteristics
    font = CONSOLE_FONT_INFOEX()
    font.cbSize = sizeof(CONSOLE_FONT_INFOEX)
    res = get_current_console_font_ex_func(stdout, False, byref(font))
    if not res:
        print("{:s} error: {:d}".format(get_current_console_font_ex_func.__name__, get_last_error_func()))
        return
    # Display font information
    print("Console information for {:}".format(font))
    for field_name, _ in font._fields_:
        field_data = getattr(font, field_name)
        if field_name == "dwFontSize":
            print("    {:s}: {{X: {:d}, Y: {:d}}}".format(field_name, field_data.X, field_data.Y))
        else:
            print("    {:s}: {:}".format(field_name, field_data))

    height = 40
    # Alter font height
    font.dwFontSize.X = 10  # Changing X has no effect (at least on my machine)
    font.dwFontSize.Y = height
    # Apply changes
    res = set_current_console_font_ex_func(stdout, False, byref(font))
    if not res:
        print("{:s} error: {:d}".format(set_current_console_font_ex_func.__name__, get_last_error_func()))
        return
    print("OMG! The window changed :)")
    # Get current font characteristics again and display font size
    res = get_current_console_font_ex_func(stdout, False, byref(font))
    if not res:
        print("{:s} error: {:d}".format(get_current_console_font_ex_func.__name__, get_last_error_func()))
        return
    print("\nNew sizes    X: {:d}, Y: {:d}".format(font.dwFontSize.X, font.dwFontSize.Y))


# -------------------------------------------------------------------------------------


# kana = '｡｢｣､･ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝﾞ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

choices = digits + ascii_uppercase

print(GREEN)


# TODO subclass drop from Object
class Drop(object):

    def __init__(self):
        self.x = random.randint(0, cols - 1)
        self.y = random.randint(-rows, -1)
        self.yspeed = 1
        self.length = random.randint(rows // 2, rows - 2)
        self.movecount = 7
        self.chars = deque([])
        for i in range(self.length):
            char = ''.join(random.choice(choices))
            self.chars.append(char)

    def fall(self):
        self.y += self.yspeed
        self.chars.rotate(-1)
        for j in range(self.length):
            # change character:
            if self.movecount % (random.randint(1, 30)) == 0:
                self.chars[j] = ''.join(random.choice(choices))
        if self.y > rows + self.length:
            self.x = random.randint(0, cols - 1)
            self.y = random.randint(5 - rows, -5)

    def show(self):
        start = end = 0
        if self.y == 0:
            pass
        elif 0 < self.y < self.length:
            start = 0
            end = self.y
        elif self.length <= self.y < rows:
            start = self.y - self.length
            end = self.y
        elif rows <= self.y:
            start = self.y - self.length
            end = rows
        return start, end


rows = 20
cols = 20
drops = 10
speed = 0.05

if __name__ == '__main__':
    sys.stdout.write(HIDE_CURSOR)
    matrix = [[[0, ' '] for j in range(cols)] for i in range(rows)]
    drop = dict()
    for i in range(drops):
        drop[i] = Drop()
    xy = [0 for i in range(4)]
    while True:
        os.system('cls')
        # drop the drops:
        for i in range(drops):
            drop[i].fall()

            y1, y2 = drop[i].show()
            # change matrix numbers:
            if y1 == y2:
                matrix[rows - 1][drop[i].x] = [0, ' ']
            if y1 == 0:
                for j in range(y2 - 1, y1 - 1, -1):
                    matrix[j][drop[i].x] = [1, drop[i].chars[j - (y2 - 1) - 1]]
                    if y2 > drop[i].length:
                        matrix[y1 - 1][drop[i].x] = [0, ' ']
            else:
                for j in range(y1, y2):
                    matrix[j][drop[i].x] = [1, drop[i].chars[j - y1]]
                    if y2 > drop[i].length:
                        matrix[y1 - 1][drop[i].x] = [0, ' ']
        # draw matrix:
        for j, y in enumerate(matrix):
            for i, x in enumerate(y):
                if x[0] == 1:
                    # head:
                    if j < len(matrix) - 1 and matrix[j + 1][i][0] == 0:
                        sys.stdout.write(HEAD + x[1] + ENDC)
                    elif j < len(matrix) - 2 and matrix[j + 1][i][0] == 1 and matrix[j + 2][i][0] == 0:
                        sys.stdout.write(SECHEAD + x[1] + ENDC)
                    elif j < len(matrix) - 3 and matrix[j + 1][i][0] == 1 and matrix[j + 2][i][0] == 1 and \
                            matrix[j + 3][i][0] == 0:
                        sys.stdout.write(THRDHEAD + x[1] + ENDC)
                    # tail:
                    elif j > 0 and matrix[j - 1][i][0] == 0:
                        sys.stdout.write(TAIL + x[1] + ENDC)
                    elif j > 1 and matrix[j - 1][i][0] == 1 and matrix[j - 2][i][0] == 0:
                        sys.stdout.write(SECTAIL + x[1] + ENDC)
                    elif j > 2 and matrix[j - 1][i][0] == 1 and matrix[j - 2][i][0] == 1 and matrix[j - 3][i][0] == 0:
                        sys.stdout.write(THRDTAIL + x[1] + ENDC)
                    # middle:
                    else:
                        sys.stdout.write(GREEN + x[1] + ENDC)
                        sys.stdout.flush()
                else:
                    sys.stdout.write(' ')
                    sys.stdout.flush()

            sys.stdout.write('\n' + HIDE_CURSOR)
            sys.stdout.flush()

        time.sleep(speed)
