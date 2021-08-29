import time
import sys
import sys
import time
import threading
import math
from collections import deque
import numpy as np
import math
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

HIDE_CURSOR = '\x1b[?25l'
SHOW_CURSOR = '\x1b[?25h'


def snipper(anim_num=1, duraion=10, speed=0.25):
    elapsed_time = 0
    sleep_secs = speed

    while True:
        char_list = {1: '│╱―╲',
                     2: '◷◶◵◴',
                     3: '◐◓◑◒',
                     4: '▖▘▝▗',
                     5: '▪▫',
                     6: '┤┘┴└├┌┬┐',
                     7: '⣾⣽⣻⢿⡿⣟⣯⣷',
                     8: "⠁⠂⠄⡀⢀⠠⠐⠈",
                     9: ['⠁⠂⠄⡀', '⠂⠄⡀⡀', '⠄⡀⡀⠄', '⡀⡀⠄⠂', '⡀⠄⠂⠁', '⠄⠂⠁⠁', '⠂⠁⠁⠂', '⠁⠁⠂⠄'],
                     10: ['   ', '.  ', '.. ', '...'],
                     11: ["◜ ", "◝ ", "◞ ", "◟ "],
                     12: ' ▁▃▅▆▇▆▅▃▁',
                     13: ['〉  ', ' 〉 ', '  〉', '  〈', ' 〈 ', '〈  '],
                     14: ['👉    👌', ' 👉   👌', '  👉  👌', '   👉 👌', '    👉👌', '     👏', '     👏'],
                     15: '😂😁😀🙂😐😑😐🙂😀😁',
                     16: ['    ☢    ',
                          '    ☢    ',
                          '    ❂    ',
                          '   (◉)   ',
                          '  ((⬤))  ',
                          ' (( 〇 )) ',
                          '((  ◯  ))',
                          '(        )',
                          '          '],
                     17: ['➵     💗', ' ➵    💗', '  ➵   💗', '   ➵  💗', '    ➵ 💗', '     ➵💗', '      💘'],
                     18: ['(\˙-˙)\ ┳━━━┳                   ',
                          '(\˙-˙)\ ┳━━━┳                   ',
                          '(\°▫°)\ ┳━━━┳                   ',
                          '(-°□°)-     ]                   ',
                          '( ╯°□° )╯   ︵ ┻━━━┻            ',
                          '( ╯°□° )╯          [            ',
                          '( ╯°□° )╯        ︵ ┳━━━┳       ',
                          '( ╯°□° )╯               ]       ',
                          '( ╯°□° )╯              ︵ ┻━━━┻ ',
                          '(╯°□°)╯                        [',
                          '(-°-°)-                         ',
                          '(\˙-˙)\                         ',
                          '(\˙-˙)\                         '],
                     19: ['│▌        │',
                          '│█        │',
                          '│█▌       │',
                          '│██       │',
                          '│▐█▌      │',
                          '│ ██      │',
                          '│ ▐█▌     │',
                          '│  ██     │',
                          '│  ▐█▌    │',
                          '│   ██    │',
                          '│   ▐█▌   │',
                          '│    ██   │',
                          '│    ▐█▌  │',
                          '│     ██  │',
                          '│     ▐█▌ │',
                          '│      ██ │',
                          '│      ▐█▌│',
                          '│       ██│',
                          '│       ▐█│',
                          '│        █│',
                          '│        ▐│',
                          '│         │'],
                     20: ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
                     21: ["▐⠂       ▌", "▐⠈       ▌", "▐ ⠂      ▌", "▐ ⠠      ▌", "▐  ⡀     ▌", "▐  ⠠     ▌",
                          "▐   ⠂    ▌", "▐   ⠈    ▌", "▐    ⠂   ▌", "▐    ⠠   ▌", "▐     ⡀  ▌", "▐     ⠠  ▌",
                          "▐      ⠂ ▌", "▐      ⠈ ▌", "▐       ⠂▌", "▐       ⠠▌", "▐       ⡀▌", "▐      ⠠ ▌",
                          "▐      ⠂ ▌", "▐     ⠈  ▌", "▐     ⠂  ▌", "▐    ⠠   ▌", "▐    ⡀   ▌", "▐   ⠠    ▌",
                          "▐   ⠂    ▌", "▐  ⠈     ▌", "▐  ⠂     ▌", "▐ ⠠      ▌", "▐ ⡀      ▌", "▐⠠       ▌"],
                     22: ["⢄", "⢂", "⢁", "⡁", "⡈", "⡐", "⡠"],
                     23: ["⢹", "⢺", "⢼", "⣸", "⣇", "⡧", "⡗", "⡏"],
                     24: ["∙∙∙", "●∙∙", "∙●∙", "∙∙●", "∙∙∙"],
                     25: ["█", "▓", "▒", "░"],
                     26: ["█", "▀", "█", "▄"],
                     27: ["( ●    )", "(  ●   )", "(   ●  )", "(    ● )", "(     ●)", "(    ● )", "(   ●  )",
                          "(  ●   )", "( ●    )", "(●     )"],
                     28: [" |     ", "  /    ", "   _   ", '    \  ', "     | ", '    \  ', "   _   ", "  /    "]
                     }

        for l in char_list[anim_num]:
            sys.stdout.write('\r' + 'Loading ' + l + ' ')
            sys.stdout.flush()
            # sys.stdout.write('\b')
            time.sleep(sleep_secs)
            elapsed_time += sleep_secs
            if elapsed_time > duraion:
                sys.stdout.write('\r' + 'Done!')
                sys.stdout.flush()
                break
        if elapsed_time > duraion:
            break


def loading_bar_sample(process_len=20, bar_len=20, bar_type=1):
    types = {1: ['█', '▒'], 2: ['■', '□'], 3: ['⬛', '⬜'], 4: ['▰', '▱'], 5: ['▮', '▯'], 6: ['⚫', '⚪'],
             7: ['⣿', '⣉']}
    loaded = types[bar_type][0]
    not_loaded = types[bar_type][1]
    n = bar_len
    n_count = 0
    for i in range(process_len + 1):
        if int(i * n / process_len) != n_count:
            n_count += math.ceil(n / process_len)
        if n_count > n:
            n_count = n
        char = loaded * n_count

        slimit = ''
        elimit = ''
        if bar_type == 7:
            slimit = '⢸'
            elimit = '⡇'
        sys.stdout.write('\r' + 'Downloading Files ' + slimit +
                         char + elimit.rjust(n - n_count, not_loaded) +
                         ' ' + str(float(i * 100 / process_len)) + '%' + HIDE_CURSOR)
        time.sleep(0.05)
        sys.stdout.flush()

    print('\nDownload Completed')


# loading_bar_sample(process_len=20 , bar_len=50)


def loading_bar(stage=None, process_length=None, bar_len=20, message='Downloading Files'):
    # safety
    if type(stage) != int:
        raise TypeError('stage type should be int')
    if type(process_length) != int:
        raise TypeError('process_length type should be int')
    if type(bar_len) != int:
        raise TypeError('bar_len type should be int')
    if type(message) != str:
        raise TypeError('message type should be str')
    if process_length is None:
        raise ValueError('process_length is not determined')
    if stage is None:
        raise ValueError('stage is not determined')
    if stage >= process_length:
        raise ValueError('stage is equal or bigger than process_length')

    # calculations
    n = bar_len
    n_count = 0
    n_count += math.ceil(stage * n / process_length)
    if n_count > n:
        n_count = n
    char = '█' * n_count
    sys.stdout.write('\r' + message + ' ' +
                     char + ''.rjust(n - n_count, '▒') +
                     ' ' + str(int(stage * 100 / process_length)) + '%')
    sys.stdout.flush()
    if stage == process_length - 1:
        time.sleep(0.5)
        sys.stdout.write('\r' + message + ' ' + '█' * bar_len + ' 100%')
        sys.stdout.flush()
        print('\n' + message + ' Completed')


def dot_snipper_base():
    chars = ['⠁', '⠂', '⠄', '⡀']
    txt = list('    ')
    pos = np.arange(0, len(txt))
    cases = {0: 3, 1: 2, 2: 1, 3: 0}
    # pos.reverse()
    # print(pos)
    while True:
        # print(pos)
        for i, d in enumerate(pos):
            txt[i] = chars[d]
        out = ''.join(txt)
        sys.stdout.write('\r' + out)
        sys.stdout.flush()
        time.sleep(0.25)
        pos = np.roll(pos, -1)
        pos[-1] = cases[pos[-1]]


def rounder(num):
    if num > 0.7:
        return 1
    if 0 < num <= 0.7:
        return 0.5
    if -0.7 < num <= 0:
        return -0.5
    if num <= -0.7:
        return -1


def dot_snipper(length=8, duraion=10, speed=0.1, char_type=1, stop=True):
    # '⠁⠂⠄⡀'
    # '⣾⣽⣻⢿'
    elapsed_time = 0
    sleep_secs = speed
    pi = math.pi
    chars = {1: ['⠁', '⠂', '⠄', '⡀'],
             2: ['⣾', '⣽', '⣻', '⢿'],
             3: ['▉', '▆', '▃', '▁'],
             4: ['☱', '☲', '☴', '☰'],
             5: ['☶', '☵', '☳', '☷'],
             6: ['┋', '┇', '╏', '┃'],
             7: ['˦', '˧', '˨', '˩']
             }
    txt = [' ' for i in range(length)]
    cases = {1: 0, 0.5: 1, -0.5: 2, -1: 3}
    d = [x for x in range(length)]
    denum = 4
    angle = [pi / 6 + x * pi / denum for x in d]
    while True:
        pos = [math.sin(rad) for rad in angle]
        for i, d in enumerate(txt):
            pos[i] = rounder(pos[i])
            txt[i] = chars[char_type][cases[pos[i]]]
        out = ''.join(txt)
        sys.stdout.write('\r' + 'Loading ' + out + HIDE_CURSOR)
        sys.stdout.flush()
        time.sleep(speed)
        angle = [rad + pi / denum for rad in angle]

        elapsed_time += sleep_secs
        if stop and elapsed_time > duraion:
            break


def rounder2(num):
    if num > 0.7:
        return 1
    if 0.3 < num <= 0.7:
        return 0.5
    if -0.3 < num <= 0.3:
        return 0
    if -0.7 < num <= -0.3:
        return -0.5
    if num <= -0.7:
        return -1


def dot_snipper2(length=8, duraion=10, speed=0.1, char_type=1):
    # '⠁⠂⠄⡀'
    # '⣾⣽⣻⢿'
    elapsed_time = 0
    sleep_secs = speed
    pi = math.pi
    chars = {1: ['˥', '˦', '˧', '˨', '˩']
             }
    txt = [' ' for i in range(length)]
    cases = {1: 0, 0.5: 1, 0: 2, -0.5: 3, -1: 4}
    d = [x for x in range(length)]
    denum = 5
    angle = [pi / (denum + 1) + x * pi / denum for x in d]
    while True:
        pos = [math.sin(rad) for rad in angle]
        for i, d in enumerate(txt):
            pos[i] = rounder2(pos[i])
            txt[i] = chars[char_type][cases[pos[i]]]
        out = ''.join(txt)
        sys.stdout.write('\r' + 'Loading ' + out)
        sys.stdout.flush()
        time.sleep(speed)
        angle = [rad + pi / denum for rad in angle]

        elapsed_time += sleep_secs
        if elapsed_time > duraion:
            break


'_‾'
if __name__ == '__main__':
    # for i in range(1, 20):
    #     snipper(anim_num=i, speed=0.15, duraion=3)

    # n = int(input('number: '))
    # m = float(input('speed: '))
    # snipper(anim_num=28, duraion=5, speed=0.05)

    loading_bar_sample(process_len=1000, bar_len=50, bar_type=1)

    # for i in range(1,8):
    #     dot_snipper(length=8 , duraion=10 , speed=0.08 , char_type=i)

    # dot_snipper(length=8 , duraion=10 , speed=0.08 , char_type=1 , stop=False)
    # print('\u2103')
    # dot_snipper2(length=6, duraion=20, speed=0.1, char_type=1)
