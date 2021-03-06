from tkinter import *


incr = 2
size = incr * 10
posX = 1
posY = 1
map = [[]] * 100

for value in range(0, 100):
    map[value] = [0] * 100



def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x * (incr), 0, x * (incr), canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y * (incr), canvas_width, y * (incr), fill="#476042")

def right():
    global posX
    global posY
    if (map[posY][posX + 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX += 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        print('Vous avez parcouru : '+nbreCase' !')
        exit(0)

def left():
    global posX
    global posY
    if (map[posY][posX - 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX -= 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        print('Vous avez parcouru : '+nbreCase' !')
        exit(0)

def up():
    global posY
    global posX
    if (map[posY - 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY -= 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        print('Vous avez parcouru : '+nbreCase' !')
        exit(0)

def down():
    global posY
    global posX
    if (map[posY + 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY += 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        print('Vous avez parcouru : '+nbreCase' !')
        exit(0)



dir = []

#def totalBlockedTop():
#    if(map[posY - 1][posX]==1 && map[posY][posX + 1]==1 && map[posY][posX - 1]==1):
#        return True
#    return False

#def totalBlockedDown():
#    if(map[posY + 1][posX]==1 && map[posY][posX + 1]==1 && map[posY][posX - 1]==1):
#        return True
#    return False

#def totalBlockedRight():
#    if(map[posY - 1][posX]==1 && map[posY + 1][posX]==1 && map[posY][posX + 1]==1):
#        return True
#    return False

#def totalBlockedLeft():
#    if(map[posY - 1][posX]==1 && map[posY + 1][posX]==1 && map[posY][posX - 1]==1):
#        return True
#    return False
def prioUp():
    if(map[posY - 1][posX]==2):
        up()
        dir.append(2)
        return
    elif(map[posY][posX + 1]==2):
        right()
        dir.append(1)
        return
    elif(map[posY + 1][posX]==2):
        down()
        dir.append(4)
        return
    elif(map[posY][posX - 1]==2):
        left()
        dir.append(3)
        return
    elif(map[posY][posX + 1]==0):
        right()
        dir.append(1)
        return
    elif(map[posY - 1][posX]==0):
        up()
        dir.append(2)
        return
    elif(map[posY][posX - 1]==0):
        left()
        dir.append(3)
        return
    elif(map[posY + 1][posX]==0):
        down()
        dir.append(4)
        return
    elif(dir[-1]==2):
        down()
        dir.pop()
        return
    elif(dir[-1]==1):
        left()
        dir.pop()
        return
    elif(dir[-1]==4):
        up()
        dir.pop()
        return
    elif(dir[-1]==3):
        right()
        dir.pop()
        return

def prioDown():
    if(map[posY + 1][posX]==2):
        down()
        dir.append(4)
        return
    elif(map[posY][posX + 1]==2):
        right()
        dir.append(1)
        return
    elif(map[posY - 1][posX]==2):
        up()
        dir.append(2)
        return
    elif(map[posY][posX - 1]==2):
        left()
        dir.append(3)
        return
    elif(map[posY + 1][posX]==0):
        down()
        dir.append(4)
        return
    elif(map[posY][posX + 1]==0):
        right()
        dir.append(1)
        return
    elif(map[posY - 1][posX]==0):
        up()
        dir.append(2)
        return
    elif(map[posY][posX - 1]==0):
        left()
        dir.append(3)
        return
    elif(dir[-1]==4):
        up()
        dir.pop()
        return
    elif(dir[-1]==1):
        left()
        dir.pop()
        return
    elif(dir[-1]==2):
        down()
        dir.pop()
        return
    elif(dir[-1]==3):
        right()
        dir.pop()
        return

def prioLeft():
        if(map[posY][posX - 1]==2):
            left()
            dir.append(3)
            return
        elif(map[posY - 1][posX]==2):
            up()
            dir.append(2)
            return
        elif(map[posY][posX + 1]==2):
            right()
            dir.append(1)
            return
        elif(map[posY + 1][posX]==2):
            down()
            dir.append(4)
            return
        elif(map[posY][posX - 1]==0):
            left()
            dir.append(3)
            return
        elif(map[posY - 1][posX]==0):
            up()
            dir.append(2)
            return
        elif(map[posY][posX + 1]==0):
            right()
            dir.append(1)
            return
        elif(map[posY + 1][posX]==0):
            down()
            dir.append(4)
            return
        elif(dir[-1]==3):
            right()
            dir.pop()
            return
        elif(dir[-1]==2):
            down()
            dir.pop()
            return
        elif(dir[-1]==1):
            left()
            dir.pop()
            return
        elif(dir[-1]==4):
            up()
            dir.pop()
            return

def prioRight():
    if(map[posY][posX + 1]==2):
        right()
        dir.append(1)
        return
    elif(map[posY - 1][posX]==2):
        up()
        dir.append(2)
        return
    elif(map[posY][posX - 1]==2):
        left()
        dir.append(3)
        return
    elif(map[posY + 1][posX]==2):
        down()
        dir.append(4)
        return
    elif(map[posY][posX + 1]==0):
        right()
        dir.append(1)
        return
    elif(map[posY - 1][posX]==0):
        up()
        dir.append(2)
        return
    elif(map[posY][posX - 1]==0):
        left()
        dir.append(3)
        return
    elif(map[posY + 1][posX]==0):
        down()
        dir.append(4)
        return
    elif(dir[-1]==1):
        left()
        dir.pop()
        return
    elif(dir[-1]==2):
        down()
        dir.pop()
        return
    elif(dir[-1]==3):
        right()
        dir.pop()
        return
    elif(dir[-1]==4):
        up()
        dir.pop()
        return
nbreCase=0
def algo(value):
    nbreCase++
    if(posY>21):
        prioDown()
        return
    elif(posY<=21 and posX<47):
        prioRight()
        return
    elif(posY<=21 and posX>=47):
        prioLeft()
        return









def setACaseXY(X, Y, color):
    points = [X * size, Y * size, size * (X + 1), Y * size, size * (X + 1), size * (Y + 1), X * size, size * (Y + 1)]
    w.create_polygon(points, outline="#476042", fill=color, width=4)



master = Tk()
canvas_width = 1000
canvas_height = 1000
w = Canvas(master,
           width=1000,
           height=1000)











path = 'map.txt'
with open(path) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       x = line.find('x')
       while x != -1:
           setACaseXY(x, cnt, 'red')
           map[cnt][x] = 1
           x = line.find('x', x + 1)
       line = fp.readline()
       cnt += 1

w.pack()

setACaseXY(47, 21, 'green')
map[21][47] = 2


for value in range(0, 1000):
    master.after(value * 100, algo, value)

checkered(w,10)

mainloop()
