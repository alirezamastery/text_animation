import tkinter as tk
import random
import numpy as np
import time


class window:

    def __init__(self):
        self.end = False
        self.stars_number = 50

        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.resizable(0 , 0)

        self.width = 500
        self.height = 500

        # self.width = self.root.winfo_screenwidth()
        # self.height = self.root.winfo_screenheight()

        # self.root.attributes("-fullscreen" , True)
        # self.root.config(cursor="none")

        # pad = 3
        # self._geom = '1000x500+0+0'
        # self.root.geometry("{0}x{1}+0+0".format(
        #         self.root.winfo_screenwidth() - pad , self.root.winfo_screenheight() - pad))
        # self.root.bind('<Escape>' , self.toggle_geom)

        self.canvas = tk.Canvas(self.root , bg='black' , width=self.width , height=self.height ,
                                bd=0 , highlightthickness=0 , relief='ridge')
        self.canvas.create_line(self.width / 2 , 0 , self.width / 2 , self.height , fill='green')
        self.canvas.create_line(0 , self.height / 2 , self.width , self.height / 2 , fill='green')
        self.canvas.pack()

        self.stars = list()

        self.create_stars()

        self.root.mainloop()

    def create_stars(self):
        self.root.protocol("WM_DELETE_WINDOW" , self.brk)

        for i in range(self.stars_number):
            self.stars.append(star(self.canvas , self.width , self.height))

        self.root.after(0 , self.display())

    def display(self):
        while not self.end:
            for i in range(self.stars_number):
                if self.end:
                    break
                # self.stars[i].move()
            self.root.update()
            time.sleep(0.1)
        else:
            try:
                self.root.destroy()
            except:
                pass

    # def toggle_geom(self , event):
    #     self.root.attributes("-fullscreen" , False)
    #     geom = self.root.winfo_geometry()
    #     # print(geom , self._geom)
    #     self.root.geometry(self._geom)
    #     self._geom = geom

    def brk(self):
        self.end = True


def translate(value , leftMin , leftMax , rightMin , rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


class star:

    def __init__(self , canvas , width , height):
        self.canvas = canvas
        self.width = width
        self.height = height

        self.x = random.randrange(0 , self.width)
        # self.x = translate(self.x , -self.width , self.width , self.width // 2 , self.width)
        self.y = random.randrange(0 , self.height)
        # self.y = translate(self.y , -self.height , self.height , self.height // 2 , self.height)

        self.zx = self.width
        self.zy = self.width

        self.sx = np.interp(self.x / self.zx , [0 , 1] , [0 , self.width])
        self.sy = np.interp(self.y / self.zy , [0 , 1] , [0 , self.height])

        # self.circle = self.canvas.create_oval(self.x , self.y , self.x + 8 , self.y + 8 , fill='white')

        self.zx2 = self.zx - 100
        self.zy2 = self.zy - 100
        self.sx2 = np.interp(self.x / self.zx2 , [0 , 1] , [0 , self.width])
        self.sy2 = np.interp(self.y / self.zy2 , [0 , 1] , [0 , self.height])

        self.canvas.create_line(self.x , self.y , self.sx2 , self.sy2 , fill='white')

        print(self.x , self.sx , self.y , self.sy)

    def move(self):
        sx_old = self.sx
        sy_old = self.sy

        if self.zx > 1 and self.zy > 1:

            if self.x >= self.width / 2 and self.y >= self.height / 2:
                self.zx -= 1
                self.zy -= 1
                self.sx = np.interp(self.sx / self.zx , [0 , 1] , [0 , self.width])
                self.sy = np.interp(self.sy / self.zy , [0 , 1] , [0 , self.height])
                self.canvas.move(self.circle , self.sx - sx_old , self.sy - sy_old)
                # self.canvas.create_oval(self.sx , self.sy , self.sx + 8 , self.sy + 8 , fill='white')

            elif self.x < self.width / 2 and self.y >= self.height / 2:
                self.zx -= 1
                self.zy -= 1
                self.sx = np.interp(self.sx / self.zx , [0 , 1] , [0 , self.width])
                self.sy = np.interp(self.sy / self.zy , [0 , 1] , [0 , self.height])
                self.canvas.move(self.circle , sx_old - self.sx , self.sy - sy_old)
                # self.canvas.create_oval(-self.sx , self.sy , self.sx + 8 , self.sy + 8 , fill='white')

            elif self.x < self.width / 2 and self.y < self.height / 2:
                self.zx -= 1
                self.zy -= 1
                self.sx = np.interp(self.sx / self.zx , [0 , 1] , [0 , self.width])
                self.sy = np.interp(self.sy / self.zy , [0 , 1] , [0 , self.height])
                self.canvas.move(self.circle , sx_old - self.sx , sy_old - self.sy)
                # self.canvas.create_oval(-self.sx , -self.sy , self.sx + 8 , self.sy + 8 , fill='white')

            elif self.x >= self.width / 2 and self.y < self.height / 2:
                self.zx -= 1
                self.zy -= 1
                self.sx = np.interp(self.sx / self.zx , [0 , 1] , [0 , self.width])
                self.sy = np.interp(self.sy / self.zy , [0 , 1] , [0 , self.height])
                self.canvas.move(self.circle , self.sx - sx_old , sy_old - self.sy)
                # self.canvas.create_oval(self.sx , -self.sy , self.sx + 8 , self.sy + 8 , fill='white')

        print(self.x , self.sx , self.y , self.sy)


if __name__ == '__main__':
    print(translate(0.5 , 0 , 1 , 0 , 100))
    window()
