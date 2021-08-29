import ctypes
import sys

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11) , 7)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.WARNING + "colors everywhere" + bcolors.HEADER)
print('\033[32m' + '⌈' + '¯' * 18 + '⌉' + ' Hello' + '\033[0m')
print('⌊' + '_' * 18 + '⌋' + ' Hello')
print('┌' + '─' * 18 + '┐' + 'Hello')
print('└' + '─' * 18 + '┘')
print('\u001b[31m' + '┌' + '─' * 18 + '┐' + 'Hello')
print('│' + ' ' * 18 + '│' + 'Hello')
print('└' + '─' * 18 + '┘')
print('\u001b[34;1m' + '╔' + '═' * 18 + '╗' + 'Hello')
txt = ' the answer ho'
print('║' + txt.ljust(18 - len(txt) , ' ') + '║'.rjust(19 - len(txt) , ' ') + 'Hello')
print('╚' + '═' * 18 + '╝')

print('\u001b[37m' + '┌─┬┐  ╔═╦╗  ╓─╥╖  ╒═╤╕')
print('│ ││  ║ ║║  ║ ║║  │ ││')
print('├─┼┤  ╠═╬╣  ╟─╫╢  ╞═╪╡')
print('└─┴┘  ╚═╩╝  ╙─╨╜  ╘═╧╛')
print('\u001b[35m' + '┌───────────────────┐')
print('│  ╔═══╗ Some Text  │▒')
print('│  ╚═╦═╝ in the box │▒')
print('╞═╤══╩══╤═══════════╡▒')
print('│ ├──┬──┤  hello    │▒')
print('│ └──┴──┘  hello    │▒')
print('└───────────────────┘▒')
print(' ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')

for i in range(0 , 16):
    for j in range(0 , 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")

for i in range(0 , 16):
    for j in range(0 , 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")

x = input('press any key to fuck off:')
print('\u001b[1A' + u"\u001b[1000D" + '\u001b[2K' + "\u001b[0m" + 'I just tricked you')
print('I just tricked you')
y = input(bcolors.WARNING + 'press any key again:')
