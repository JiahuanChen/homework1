"""Python2
Need to tpye 'python readFASTAforPY2.py filename' 
or 'python readFASTAforPY2.py filename' to run this script.
Or add "alias readFASTA='python readFASTAforPY2.py'" to '~/.bashrc'.
Thus this can be run by typing 'readFASTA filename'.
"""

import sys
import string

#Number of characters in one line
length = 70

# check whether the file exist and is FASTA
def checkfile(filename):
    try:
        if open(filename).readline()[0] == '>':
            return open(filename);
        else: 
            print 'Not a FASTA file.'             
            return 0
    except IOError:
        print 'File not exist.'
        return  0;

# Check the command, like weather filename is given.
# Reply different situations with different answers.
# Return task: 0 for input error; 1 for complement and reverse;
# 2 for RNA transcription
def checkinput(arg):
    if len(arg) < 2:
        print 'Didn\'t enter filename.' 
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
                print 'Wrong function.' 
                return 0,0
    elif len(arg) >2:
        print 'Too many input.' 
        return 0,0

#reverse and complement the sequences
def rev_com(sequence):
    for i in range(0,len(sequence)):
        sequence[i] = sequence[i][::-1]
        line = list(sequence[i])
        for j in range(0,len(line)):
            if   line[j] == 'A': line[j] = 'T'
            elif line[j] == 'T': line[j] = 'A'
            elif line[j] == 'C': line[j] = 'G'
            elif line[j] == 'G': line[j] = 'C'
        sequence[i] = ''.join(line)
    return sequence

# read name and sequence from file
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
            sequence[count] += line
    for i in range(0,count+1):
        sequence[i] = sequence[i].replace('\n','')
	# I obtained the contant from FASTA file that I download
	# and wrote is twice into test file for testing 2 sequences.
	# However, the test file ends a line with \r\n instead of \n.
	sequence[i] = sequence[i].replace('\r','')
    return name,sequence

def printseq(s):
    for i in range(0,len(s),length):
        print(s[i:i+length])
    print('-'*length)

def output(name,sequence):
    for i in range(0,len(name)):
        print 'Name %d: %s, %d bp' \
        %((i+1), name[i][1:],len(sequence[i]))
        print '\nSequence %d:'%(i+1)
        printseq(sequence[i])
    
def func1(file):
    name,sequence = getcontant(file)
    sequence = rev_com(sequence)
    return name,sequence

def func2(sequence):
    i = 0
    for s in sequence:
        sequence[i] = s.replace('T', 'U')
        i += 0
    return sequence
  
# entrence of the sript
if __name__ == '__main__':
    file,task = checkinput(sys.argv)
    if task == 1:
        # get reversed and complemented sequence
        # and its name
        name,sequence = func1(file)
        output(name, sequence)
    elif task == 2:
        # transcript DNA to RNA
        name,sequence = func1(file)
        sequence = func2(sequence)
        output(name, sequence)
    elif task == 0:
        pass
