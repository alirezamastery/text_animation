import sys
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

# kana = '｡｢｣､･ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝﾞ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

choices = digits + ascii_uppercase

print(GREEN)


class Drop:

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
        os.system('clear')
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
