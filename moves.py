import cube

def R():
    cube.red = cube.red[::-1]
    cube.red = cube.red.transpose()

    tempg = [cube.green[0][2],cube.green[1][2],cube.green[2][2]]
    tempw = [cube.white[0][2],cube.white[1][2],cube.white[2][2]]
    tempb = [cube.blue[2][0],cube.blue[1][0],cube.blue[0][0]]
    tempy = [cube.yellow[0][2],cube.yellow[1][2],cube.yellow[2][2]]

    tempw,tempb,tempy,tempg = tempg,tempw,tempb,tempy

    cube.green[0][2],cube.green[1][2],cube.green[2][2] = tempg[0],tempg[1],tempg[2]
    cube.white[0][2],cube.white[1][2],cube.white[2][2] = tempw[0],tempw[1],tempw[2]
    cube.blue[2][0],cube.blue[1][0],cube.blue[0][0] = tempb[0],tempb[1],tempb[2]
    cube.yellow[0][2],cube.yellow[1][2],cube.yellow[2][2] = tempy[0],tempy[1],tempy[2]

def L():
    cube.orange = cube.orange[::-1]
    cube.orange = cube.orange.transpose()

    tempg = [cube.green[0][0],cube.green[1][0],cube.green[2][0]]
    tempw = [cube.white[0][0],cube.white[1][0],cube.white[2][0]]
    tempb = [cube.blue[2][2],cube.blue[1][2],cube.blue[0][2]]
    tempy = [cube.yellow[0][0],cube.yellow[1][0],cube.yellow[2][0]]

    tempw,tempb,tempy,tempg = tempb,tempy,tempg,tempw

    cube.green[0][0],cube.green[1][0],cube.green[2][0] = tempg[0],tempg[1],tempg[2]
    cube.white[0][0],cube.white[1][0],cube.white[2][0] = tempw[0],tempw[1],tempw[2]
    cube.blue[2][2],cube.blue[1][2],cube.blue[0][2] = tempb[0],tempb[1],tempb[2]
    cube.yellow[0][0],cube.yellow[1][0],cube.yellow[2][0] = tempy[0],tempy[1],tempy[2]

def U():
    cube.white = cube.white[::-1]
    cube.white = cube.white.transpose()

    tempg = [cube.green[0][0],cube.green[0][1],cube.green[0][2]]
    tempo = [cube.orange[0][0],cube.orange[0][1],cube.orange[0][2]]
    tempb = [cube.blue[0][0],cube.blue[0][1],cube.blue[0][2]]
    tempr = [cube.red[0][0],cube.red[0][1],cube.red[0][2]]

    tempg,tempo,tempb,tempr = tempr,tempg,tempo,tempb

    cube.green[0][0],cube.green[0][1],cube.green[0][2] = tempg[0],tempg[1],tempg[2]
    cube.orange[0][0],cube.orange[0][1],cube.orange[0][2] = tempo[0],tempo[1],tempo[2]
    cube.blue[0][0],cube.blue[0][1],cube.blue[0][2] = tempb[0],tempb[1],tempb[2]
    cube.red[0][0],cube.red[0][1],cube.red[0][2] = tempr[0],tempr[1],tempr[2]

def D():
    cube.yellow = cube.yellow[::-1]
    cube.yellow = cube.yellow.transpose()

    tempg = [cube.green[2][0],cube.green[2][1],cube.green[2][2]]
    tempo = [cube.orange[2][0],cube.orange[2][1],cube.orange[2][2]]
    tempb = [cube.blue[2][0],cube.blue[2][1],cube.blue[2][2]]
    tempr = [cube.red[2][0],cube.red[2][1],cube.red[2][2]]

    tempg,tempo,tempb,tempr = tempo,tempb,tempr,tempg

    cube.green[2][0],cube.green[2][1],cube.green[2][2] = tempg[0],tempg[1],tempg[2]
    cube.orange[2][0],cube.orange[2][1],cube.orange[2][2] = tempo[0],tempo[1],tempo[2]
    cube.blue[2][0],cube.blue[2][1],cube.blue[2][2] = tempb[0],tempb[1],tempb[2]
    cube.red[2][0],cube.red[2][1],cube.red[2][2] = tempr[0],tempr[1],tempr[2]

def F():
    cube.green = cube.green[::-1]
    cube.green = cube.green.transpose()

    tempw = [cube.white[2][0],cube.white[2][1],cube.white[2][2]]
    tempo = [cube.orange[2][2],cube.orange[1][2],cube.orange[0][2]]
    tempy = [cube.yellow[0][0],cube.yellow[0][1],cube.yellow[0][2]]
    tempr = [cube.red[0][0],cube.red[1][0],cube.red[2][0]]

    tempw,tempo,tempy,tempr = tempo,tempy,tempr,tempw

    cube.white[2][0],cube.white[2][1],cube.white[2][2] = tempw[0],tempw[1],tempw[2]
    cube.orange[0][2],cube.orange[1][2],cube.orange[2][2] = tempo[0],tempo[1],tempo[2]
    cube.yellow[0][2],cube.yellow[0][1],cube.yellow[0][0] = tempy[0],tempy[1],tempy[2]
    cube.red[0][0],cube.red[1][0],cube.red[2][0] = tempr[0],tempr[1],tempr[2]

def B():
    cube.blue = cube.blue[::-1]
    cube.blue = cube.blue.transpose()

    tempw = [cube.white[0][0],cube.white[0][1],cube.white[0][2]]
    tempo = [cube.orange[0][0],cube.orange[1][0],cube.orange[2][0]]
    tempy = [cube.yellow[2][2],cube.yellow[2][1],cube.yellow[2][0]]
    tempr = [cube.red[0][2],cube.red[1][2],cube.red[2][2]]

    tempw,tempo,tempy,tempr = tempr,tempw,tempo,tempy

    cube.white[0][0],cube.white[0][1],cube.white[0][2] = tempw[0],tempw[1],tempw[2]
    cube.orange[2][0],cube.orange[1][0],cube.orange[0][0] = tempo[0],tempo[1],tempo[2]
    cube.yellow[2][0],cube.yellow[2][1],cube.yellow[2][2] = tempy[0],tempy[1],tempy[2]
    cube.red[0][2],cube.red[1][2],cube.red[2][2] = tempr[0],tempr[1],tempr[2]

def r():
    for i in range(3): 
        R()  #right

def l():
    for i in range(3):
        L() #left

def u():
    for i in range(3):
        U() #upper

def d():
    for i in range(3):
        D() #down
    
def f():
    for i in range(3):
        F() #front

def b():
    for i in range(3):
        B() #back

def R2():
    for i in range(2):
        R() #two times right

def L2():
    for i in range(2):
        L() #two times left

def U2():
    for i in range(2):
        U() #two times up

def D2():
    for i in range(2):
        D() #two times down
    
def F2():
    for i in range(2):
        F() #two times front

def B2():
    for i in range(2):
        B() #two times back