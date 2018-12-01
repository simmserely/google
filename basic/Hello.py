import sys
import os
import subprocess

'''def Hello(name):
    name = name + '!!!'
    print('Hello {}'.format(name))
    #print('Hello ' + name) #alternative way to print to screen
    #print('Hello %a' %(name)) #alternative way to print to screen'''

def Cat(filename):
    try:
        f = open(filename, 'r')
        #for line in f:
        #print(line, end='') # the end parameter removes the /n (new line) printing
        text = f.read()
        #lines = text.split('\n') # better b/c is removes '\n'
        #lines = f.readlines() # also creates a list but keeps the '\n' at the end
        print('---', filename)
        print(text)
        #f.close() # option but good for completeness
    except IOError: #helps to use an error that you know can pop up and stop the whole program
        print('IO Error', filename)

def list_files(dir):
    cmd = 'ls -l' + dir
    #print('Command to run:', cmd) # since this is running live better to test
    #return # and return before rest of program to be sure this is right
    (status, output) = subprocess.getstatusoutput(cmd)
    if status:
        sys.stderr.write('there was an error:' + output) # better syntax for printing errors through a file handler
    #'''there was an error:ls: illegal option -- .usage: ls [-ABCFGHLOPRSTUWabcdefghiklmnopqrstuwx1] [file ...]'''
    #print(sys.stderr, 'there was an error:', output) #gives you output below
    #'''<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'> there was an error: ls: illegal option -- .usage: ls [-ABCFGHLOPRSTUWabcdefghiklmnopqrstuwx1] [file ...]'''
    return
    '''filenames = os.listdir(dir)
        for filename in filenames:
            path = os.path.join(dir, filename)
            print(path)
            print(os.path.abspath(path))'''

def main():
    #list_files(sys.argv[1])
    args = sys.argv[1:]
    for arg in args:
        Cat(arg)

# This is the standard boilerplate that calls the main function in Python
if __name__ == '__main__':
    main()
