import sys

# class defination 

def hi():
    print "hello world"

if __name__=='__main__':
    for fileName in sys.argv[1:]:
        inputFile = open(fileName, 'r')
        myList = []
        for line in inputFile:
            myList.append(line.strip())
            myList.sort()
    print myList[len(myList)/2] 



    
