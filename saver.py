import os.path as pt
from errors import AlreadyIn

def save(id,msg):
    to_save = '{},{},{},{}'.format(id,msg[0],msg[1],msg[2])

    rlim = 6 if msg[2] == 7 else msg[2]
    for i in range(rlim):
        to_save = to_save + ',{}'.format(interpret(msg[i+3]))

    if pt.exists('saves/day{}.csv'.format(msg[1])):
        with open('saves/day{}.csv'.format(msg[1]),'r') as f:
            for l in f.readlines():
                if id in l:
                    raise AlreadyIn
        with open('saves/day{}.csv'.format(msg[1]),'a') as f:
            f.write(to_save + '\n')
    else:
        with open('saves/day{}.csv'.format(msg[1]),'w') as f:
            f.write(to_save + '\n')
    update_ranking(id,msg[0],msg[2])
    update_average(id,msg[0],msg[2])

def interpret(string) -> str:
    options = {
        '⬜' : 'W',
        '⬛' : 'W',
        '🟨' : 'Y',
        '🟩' : 'G'
    }

    new_string = ''
    for j in string:
        new_string = new_string + options[j]
    
    return new_string

def update_ranking(id,name,tries):
    if pt.exists('saves/overall.csv'):
        with open('saves/overall.csv','r') as f:
            lines = f.readlines()

        print('flag1')
        nl = []
        new = True
        for l in lines:
            print('flag2')
            if id in l:
                print('flag3')
                pts = int(l.split(',')[2]) + 7 - tries
                l = '{},{},{}\n'.format(str(id),name,pts)
                new = False
            nl.append(l)
        if new:
            nl[-1] = nl[-1] + '\n'
            nl.append('{},{},{}'.format(id,name,7-tries))
        nl[-1] = nl[-1].strip()
        with open('saves/overall.csv','w') as f:
            f.writelines(nl)
        
    else:
        with open('saves/overall.csv','w') as f:
            f.write('{},{},{}'.format(id,name,7-tries))

def update_average(id,name,tries):
    if pt.exists('saves/average.csv'):
        with open('saves/average.csv','r') as f:
            lines = f.readlines()

        nl = []
        new = True
        for l in lines:
            if id in l:
                games = int(l.split(',')[3]) + 1
                avg = (float(l.split(',')[2])*(games-1) + tries)/games
                l = '{},{},{},{}\n'.format(id,name,avg,games)
                new = False
            nl.append(l)
        if new:
            nl[-1] = nl[-1] + '\n'
            nl.append('{},{},{},1'.format(id,name,tries))
        nl[-1] = nl[-1].strip()
        with open('saves/average.csv','w') as f:
            f.writelines(nl)
        
    else:
        with open('saves/average.csv','w') as f:
            f.write('{},{},{},1'.format(id,name,tries))