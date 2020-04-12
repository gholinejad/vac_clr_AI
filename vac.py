import random


# direction includes right,left,up,down,suck,nop
def dirs(act):
    global visited_pieces
    if act == 'right':
        vac_pos[1] = vac_pos[1] + 1
    elif act == 'left':
        vac_pos[1] = vac_pos[1] - 1
    elif act == 'up':
        vac_pos[0] = vac_pos[0] - 1
    elif act == 'down':
        vac_pos[0] = vac_pos[0] + 1

    visited_pieces = visited_pieces + 1






def actuator(act):
    global cleaned_pieces
    if act == 'suck':
        maps[vac_pos[0]-1][vac_pos[1]-1] = 0
        cleaned_pieces = cleaned_pieces + 1





# '0' means clean & '1' means dirty
def initmap(row,col):
    global dirty_pieces
    for j in range(row):
        tmp = []
        for i in range(col):
            rand = random.randint(0,1)
            if rand == 1 :
                dirty_pieces = dirty_pieces + 1
            tmp.append(rand)               #initializing pieces with random cleanliness
        maps.append(tmp)






def allowance():
    if rows == 1 and cols != 1:    #horizontal movement
        allow = ['right','left']
    elif rows != 1 and cols == 1:  #vertical movement
        allow = ['up','down']
    elif rows == 1 and cols == 1:  #nop
        allow = []
    else:                          #two dimentional movement
        if vac_pos[0] == 1 and vac_pos[1] == 1:
            allow = ['right','down']
        elif vac_pos[0] == 1 and vac_pos[1] == cols:
            allow = ['left','down']
        elif vac_pos[0] == rows and vac_pos[1] == cols:
            allow = ['left','up']
        elif vac_pos[0] == rows and vac_pos[1] == 1:
            allow = ['right','up']
        elif vac_pos[0] == 1 :
            allow = ['right','left','down']
        elif vac_pos[0] == rows :
            allow = ['right','left','up']
        elif vac_pos[1] == 1 :
            allow = ['right','up','down']
        elif vac_pos[1] == cols :
            allow = ['left','up','down']
        else:
            allow = ['right','left','up','down']
    return allow



#main

#initializing       
maps = []
tmp_maps = []
visited_pieces = 0
dirty_pieces = 0
cleaned_pieces = 0


rows = 2                  #Row number
cols = 4                  #Column number
vac_pos = [2,1]           #Current Cursor
initmap(rows,cols)

tmp_maps = maps[:]

print('-------------------------------------')
print('Current Cursor Location :' , vac_pos)
print('-------------------------------------')
print('env. before cleaning:')
#showing the whole env.
for i in range (rows):
    print (maps[i])

print('-------------------------------------')
print('Steps and directions:')
#checking pieces
while(dirty_pieces != cleaned_pieces):      #Until all the dirty pieces are cleaned 
    if maps[vac_pos[0]-1][vac_pos[1]-1] == 1:
        actuator('suck')
    

    #print(allowance())
    allow = allowance()
    rand = random.randint(0,len(allow)-1)

    dirs(allow[rand])

    print(allow[rand], '--->' ,vac_pos)


print('-------------------------------------')
print('Environment Total Pieces :' , rows*cols)
print('visited_pieces : ', visited_pieces)
print('dirty_pieces : ', dirty_pieces)
print('cleaned_pieces : ', cleaned_pieces)
print('The Agent\'s Score : ', cleaned_pieces/visited_pieces)
print('-------------------------------------')
#showing the whole env. after cleaning
print('env. after cleaning:')
for i in range (rows):
    print (maps[i])





