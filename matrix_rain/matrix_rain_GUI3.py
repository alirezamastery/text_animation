import random
import time
import tkinter as tk
from tkinter import ttk
from collections import deque


kana = 'ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ'
kana_full = 'アイウエオカキクケコガギグゴサシスセソザジズゼゾタチツテトダヂヅデド' \
            'ナニヌネノハヒフヘホバビブベボパピプペポマミメモヤユヨラリルレロワヰヱヲ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{}~"""
greek = 'ΩΘΕΡΤΨΥΙΟΠΛΚςΗΓΦΔΣΑΖΧΞΩΒΝΜ '
digits_inverted = 'Ɛᔭ9'
ascii_uppercase_inverted = '∀𐐒ↃƎℲ⅁ſ⋊⅂ᴎԀΌᴚ⊥∩ᴧ⅄'

choices = digits + ascii_uppercase + kana
# choices = digits + ascii_uppercase_inverted + kana
# choices = digits + ascii_uppercase
# choices = '01'
# choices = greek

fonts = ['Matrix Code NFI', 'black and white', 'code predators',
         'solaria', 'Error Stencil', 'Inversionz', 'SquareFont', 'Nikkyou Sans', 'SF Square Head',
         'SF Square Head Condensed', 'AMOceanus']
font = fonts[-2]


class Drop:

    def __init__(self, canvas, speed, free_positions: list, width, height, font_size):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.speed = speed
        self.change_factor = 20
        # self.font_size = random.randint(int(font_size * 0.75) , font_size)
        self.font_size = font_size
        self.distance = int(self.font_size * 1.25)
        # generate characteristics:
        # x:
        self.x = random.choice(free_positions)
        free_positions.remove(self.x)
        # y:
        self.y1 = (self.distance // 2) + 4 - (self.height // self.distance) * self.distance * 3
        self.y2 = (self.distance // 2) + 4 - (self.height // self.distance) * self.distance
        self.y = random.randrange(self.y1, self.y2, self.distance)
        self.y1 = -(self.height // self.distance) * self.distance * 4
        self.y2 = -(self.height // self.distance) * self.distance * 2
        # length:
        self.length = random.randint(self.height // (self.font_size * 3), self.height // self.font_size)
        # speed:
        self.yspeed = random.randrange(self.distance, self.distance * 2, self.distance)
        # out of screen:
        self.bottom = (self.height // self.distance) * self.distance + self.distance // 2
        # --------------------------------------
        # create the drop:
        self.line = dict()
        self.line['blocks'] = deque([])
        self.line['chars'] = deque([])
        for i in range(self.length):
            char = ''.join(random.choice(choices))
            fill = self.color_select(self.length, i)
            self.line['blocks'].append(self.canvas.create_text(self.x, self.y + self.distance * i,
                                                               font=(font, self.font_size, 'bold'),
                                                               text=char,
                                                               fill=fill))
            self.line['chars'].append(char)

    def fall(self, free_positions: list):
        self.line['chars'].rotate(-1)
        # move down the line:
        for j in range(self.length):
            # change character:
            if random.randint(1, self.change_factor) == 1:
                char = ''.join(random.choice(choices))
                self.line['chars'][j] = char
            self.canvas.itemconfig(self.line['blocks'][j], text=self.line['chars'][j])
            # move down the character:A
            self.canvas.move(self.line['blocks'][j], 0, self.yspeed)

        # check if the line has reached the bottom:
        pos = self.canvas.coords(self.line['blocks'][0])
        if pos[1] > self.bottom:
            free_positions.append(self.x)
            self.x = random.choice(free_positions)
            free_positions.remove(self.x)
            self.y = random.randrange(self.y1, self.y2, self.distance)
            for i in range(self.length):
                self.canvas.move(self.line['blocks'][i], self.x - pos[0], self.y)

    @staticmethod
    def color_select(length, i):
        if 9 < i <= length - 4:
            return '#00ff00'
        elif i == 0:
            return '#000000'
        elif i == 1:
            return '#001a00'
        elif i == 2:
            return '#003300'
        elif i == 3:
            return '#004d00'
        elif i == 4:
            return '#006600'
        elif i == 5:
            return '#008000'
        elif i == 6:
            return '#009900'
        elif i == 7:
            return '#00b300'
        elif i == 8:
            return '#00cc00'
        elif i == 9:
            return '#00e600'
        elif length - 4 < i <= length - 2:
            return '#76fe76'
        elif i == length - 1:
            return '#ffffff'


class window():

    def __init__(self, width=1000, height=500, speed=0.01, drops=30, font_size=30):
        self.end = False
        self.width = width
        self.height = height
        self.speed = speed
        self.drops = drops
        self.font_size = font_size
        self.distance = int(self.font_size * 1.25)
        self.free_positions = []

        self.root = tk.Tk()
        self.root.geometry('300x200')
        self.root.resizable(0, 0)

        self.label_1 = tk.Label(self.root, text='Number of Drops:')
        self.label_1.place(x=150, y=40, anchor="center")

        self.entry_1 = ttk.Entry(self.root, width=15, justify='center')
        self.entry_1.insert(tk.END, '15')
        self.entry_1.place(x=150, y=70, anchor="center")

        self.button_1 = ttk.Button(self.root, pad=10, text='start', command=self.create_drops)
        self.button_1.focus_set()
        self.button_1.place(x=150, y=120, anchor="center")

        self.drop = dict()

        self.root.mainloop()

    def create_drops(self):
        self.root.protocol("WM_DELETE_WINDOW", self.brk)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.drops = int(self.entry_1.get())
        # available x positions:
        self.free_positions = [i for i in range(int(self.font_size / 3), self.width, int(self.font_size * 3 / 4))]
        # settings of window geometry:
        self.root.attributes("-fullscreen", True)
        self.root.config(cursor="none")
        pad = 3
        self._geom = '1000x500+0+0'
        self.root.geometry("{0}x{1}+0+0".format(
            self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.bind('<Escape>', self.brk)
        self.root.bind('<Motion>', self.brk)
        self.root.bind('<Key>', self.brk)
        # create canvas:
        self.canvas = tk.Canvas(self.root, bg='black', width=self.width, height=self.height,
                                bd=0, highlightthickness=0, relief='ridge')
        # for i in range(0 , self.height , self.distance):
        #     self.canvas.create_line(0 , i , self.width , i , fill='green')
        #     self.canvas.create_text(int(self.font_size / 3) , self.distance // 2 + i + 4 ,
        #                             font=(font , self.font_size , 'bold') , text='0' , fill='green')
        # self.canvas.create_line(0 , self.distance * 20 , self.width , self.distance * 20 , fill='red')
        # self.canvas.create_text(int(self.font_size / 3) , self.distance // 2 + self.distance * 20 + 4 ,
        #                         font=(font , self.font_size , 'bold') , text='0' , fill='red')
        self.canvas.pack()
        # create drops:
        for i in range(self.drops):
            self.drop[i] = Drop(self.canvas, self.speed, self.free_positions, self.width, self.height,
                                self.font_size)
        self.root.after(0, self.display())

    def display(self):
        while not self.end:
            for i in range(self.drops):
                if self.end:
                    break
                self.drop[i].fall(self.free_positions)
            self.root.update()
            time.sleep(0.001)
        else:
            try:
                self.root.destroy()
            except:
                pass

    def toggle_geom(self, event):
        self.root.attributes("-fullscreen", False)
        geom = self.root.winfo_geometry()
        # print(geom , self._geom)
        self.root.geometry(self._geom)
        self._geom = geom

    def brk(self, event):
        self.end = True
        # for i in range(self.drops):
        #     del self.drop[i]


if __name__ == '__main__':
    window()
