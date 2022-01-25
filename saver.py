import os.path as pt

def save(msg):
    to_save = '{},{},{}'.format(msg[0],msg[1],msg[2])

    for i in range(msg[2]):
        to_save = to_save + ',{}'.format(interpret(msg[i+3]))

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
        '⬛' : 'W',
        '🟨' : 'Y',
        '🟩' : 'G'
    }

    new_string = ''
    for j in string:
        new_string = new_string + options[j]
    
    return new_string

def update_ranking(name,tries):
    if pt.exists('saves/overall.csv'):
        with open('saves/overall.csv','r') as f:
            lines = f.readlines()

        nl = []
        new = True
        for l in lines:
            if name in l:
                pts = int(l.split(',')[1]) + 7 - tries
                l = '{},{}\n'.format(name,pts)
                new = False
            nl.append(l)
        if new:
            nl[-1] = nl[-1] + '\n'
            nl.append('{},{}'.format(name,7-tries))
        nl[-1] = nl[-1].strip()
        with open('saves/overall.csv','w') as f:
            f.writelines(nl)
        
    else:
        with open('saves/overall.csv','w') as f:
            f.write('{},{}'.format(name,7-tries))