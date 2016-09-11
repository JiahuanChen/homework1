# python3

import sys
import string

length = 70


def checkfile(filename):
    try:
        f = open(filename)
    except IOError:
        print('File not exist.')
        return  0;
    return f;

def checkinput(arg):
    if len(arg) < 2:            #no filename
        print('Didn\'t enter filename.')
        return 0,0;
    elif len(arg) == 2 or len(arg) == 3:         
        file = checkfile(arg[1])
        if file == 0:
            return 0,0
        elif len(arg) == 2:
            return file,1
        elif len(arg) == 3:
            if arg[2] == 'rna':
                    return file,2
            else:
                print('Wrong function.')
                return 0,0
    elif len(arg) >2:
        print('Too many input.')
        return 0,0



def rev_com(sequence):
    for i in range(0,len(sequence)):
        sequence[i] = sequence[i][::-1]
        line = list(sequence[i])
        for j in range(0,len(line)):
            if   line[j] == 'A': line[j] = 'T'
            elif line[j] == 'T': line[j] = 'A'
            elif line[j] == 'C': line[j] = 'G'
            elif line[j] == 'G': line[j] = 'C'
        line.reverse()
        sequence[i] = ''.join(line)
    return sequence

def printseq(s):
    for i in range(0,len(s),length):
        print(s[i:i+length])
    print('-'*length)


def getcontant(file):
    sequence = []
    name = []
    count = -1
    for line in file.readlines():
        if line[0] == '>':
            name.append(line.split()[0])
            sequence.append('')
            count += 1
        else:
            line = line.replace('\n','')
            sequence[count] += line
    return name,sequence


def output(name,sequence):
    for i in range(0,len(name)):
        print('Name %d: %s'%((i+1), name[i][1:]))
        print('\nSequence %d:'%(i+1))
        printseq(sequence[i])
  
def transcript(sequence):
    i = 0
    for s in sequence:
        sequence[i] = s.replace('T', 'U')
        i += 0
    return sequence
      
def func1(file):
    name,sequence = getcontant(file)
    sequence = rev_com(sequence)
    output(name,sequence)
            
def func2(file):
    name, sequence = getcontant(file)
    sequence = transcript(sequence)
    output(name, sequence)
                

if __name__ == '__main__':
    file,task = checkinput(sys.argv)
    if task == 1:
        func1(file)
    elif task == 2:
        func2(file)
    elif task == 0:
        pass
    

