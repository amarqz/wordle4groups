import os.path as pt

def save(msg):
    to_save = ''
    to_save = to_save + '{},'.format(msg[0])
    to_save = to_save + '{},'.format(msg[1])
    to_save = to_save + '{}'.format(msg[2])

    i = 0
    while i < msg[2]:
        to_save = to_save + ',{}'.format(interpret(msg[i+3]))
        i = i+1

    if pt.exists('saves/day{}.csv'.format(msg[1])):
        with open('saves/day{}.csv'.format(msg[1]),'a') as f:
            f.write(to_save + '\n')
    else:
        with open('saves/day{}.csv'.format(msg[1]),'w') as f:
            f.write(to_save + '\n')
    update_ranking(msg[0],msg[2])

def interpret(string) -> str:
    options = {
        '⬜' : 'W',
        '🟨' : 'Y',
        '🟩' : 'G'
    }

    new_string = ''
    for j in string:
        new_string = new_string + options[j]
    
    return new_string

def update_ranking(name,pts):
    if pt.exists('saves/overall.csv'):
        with open('saves/overall.csv','r') as f:
            lines = f.readlines()

        nl =[]
        for l in lines:
            if name in l:
                pts = int(l.split(',')[1]) + pts
                l = '{},{}\n'.format(name,pts)
            nl.append(l)
        with open('saves/overall.csv','w') as f:
            f.writelines(nl)
        
    else:
        with open('saves/overall.csv','w') as f:
            f.write('{},{}'.format(name,pts) + '\n')