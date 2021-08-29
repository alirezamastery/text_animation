import random
import tkinter as tk
from collections import deque

# create the list of characters to choose from:
kana = '｡｢｣､･ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝﾞ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
choices = digits + ascii_uppercase + kana


class Drop:
    def __init__(self , canvas , free_positions: list , width , height , font_size):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.movecount = 7
        self.font_size = random.randint(int(font_size * 0.75) , font_size)
        self.distance = int(self.font_size * 1.2)
        # generate characteristics:
        # x:
        self.x = random.choice(free_positions)
        free_positions.remove(self.x)
        # y:
        self.y = random.randint(-self.height * 3 , int(-self.height * 1.1))
        # length:
        self.length = random.randint(self.height // (self.font_size * 3) , self.height // self.font_size)
        # speed:
        self.yspeed = random.randrange(self.distance , self.distance * 2 , self.distance)
        # --------------------------------------
        # create the drop:
        self.line = dict()
        self.line['blocks'] = deque([])
        self.line['chars'] = deque([])
        for i in range(self.length):
            char = ''.join(random.choice(choices))
            fill = self.color_select(self.length , i)
            self.line['blocks'].append(self.canvas.create_text(self.x , self.y + self.distance * i ,
                                                               font=('White Rabbit' , self.font_size , 'bold') ,
                                                               text=char ,
                                                               fill=fill))
            self.line['chars'].append(char)

    def fall(self , free_positions: list):
        self.line['chars'].rotate(-1)
        # move down the line:
        for j in range(self.length):
            # change character:
            if 7 % (random.randint(1 , 30)) == 0:
                char = ''.join(random.choice(choices))
                self.line['chars'][j] = char
            self.canvas.itemconfig(self.line['blocks'][j] , text=self.line['chars'][j])
            # move down the character:
            self.canvas.move(self.line['blocks'][j] , 0 , self.yspeed)

        # check if the line has reached the bottom:
        pos = self.canvas.coords(self.line['blocks'][0])
        if pos[1] > int(self.height * 1.1):
            free_positions.append(self.x)
            self.x = random.choice(free_positions)
            free_positions.remove(self.x)
            self.y = random.randint(-self.height * 3 , int(-self.length * 25))
            for i in range(self.length):
                self.canvas.move(self.line['blocks'][i] , self.x - pos[0] , int(self.y - (self.height * 1.5)))

    @staticmethod
    def color_select(length , i):
        if 5 < i <= length - 4:
            return '#0dc80d'
        elif i == 0:
            return '#001300'
        elif i == 1:
            return '#001b00'
        elif i == 2:
            return '#002b00'
        elif i == 3:
            return '#004300'
        elif i == 4:
            return '#006300'
        elif i == 5:
            return '#017b01'
        elif length - 4 < i <= length - 2:
            return '#76fe76'
        elif i == length - 1:
            return '#ffffff'


class window():
    def __init__(self , speed=1 , drops=20 , font_size=30):
        self.end = False
        self.speed = speed
        self.drops = drops
        self.font_size = font_size

        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW" , self.brk)

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.free_positions = [i for i in range(int(self.font_size / 2) , self.width , self.font_size)]

        self.root.attributes("-fullscreen" , True)
        self.root.config(cursor="none")

        pad = 3
        self._geom = '1000x500+0+0'
        self.root.geometry("{0}x{1}+0+0".format(
                self.root.winfo_screenwidth() - pad , self.root.winfo_screenheight() - pad))
        self.root.bind('<Escape>' , self.toggle_geom)

        self.canvas = tk.Canvas(self.root , bg='black' , width=self.width , height=self.height ,
                                bd=0 , highlightthickness=0 , relief='ridge')
        self.canvas.pack()
        # create drops:
        self.drop = dict()
        for i in range(self.drops):
            self.drop[i] = Drop(self.canvas , self.free_positions , self.width , self.height , self.font_size)
        # start displaying:
        self.root.after(0 , self.display())
        self.root.mainloop()

    def display(self):
        if not self.end:
            for i in range(self.drops):
                self.drop[i].fall(self.free_positions)
            self.root.update()
            self.root.after(self.speed , self.display())
        else:
            try:
                self.root.destroy()
            except:
                pass

    def toggle_geom(self , event):
        self.root.attributes("-fullscreen" , False)
        geom = self.root.winfo_geometry()
        self.root.geometry(self._geom)
        self._geom = geom

    def brk(self):
        self.end = True


if __name__ == '__main__':
    window = window(speed=1 , drops=20)
