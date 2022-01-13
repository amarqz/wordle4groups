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