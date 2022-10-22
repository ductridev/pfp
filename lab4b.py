from os import getcwd

ASSETS_DIR = getcwd() + '/assets/'

def read_file():
    file = open(ASSETS_DIR + "poem.txt","r")
    for line in file:
        print(line, end = "")
    file.close()

read_file()

#Q1.2
def line_count():
    file = open(ASSETS_DIR + "poem.txt","r")
    count=0
    for line in file:
        if line[0] not in 'T':
            count+= 1
    file.close()
    print("No of lines not starting with 'T'=",count)

line_count()

#Q2.1
def word_count():
    file = open(ASSETS_DIR + "poem.txt", "rt")
    data = file.read()
    words = data.split()

    print('Number of words in text file :', len(words))
word_count()

#Q2.2
def DISPLAYWORDS():
   c=0 
   file=open(ASSETS_DIR + "poem.txt","r")
   line = file.read()
   word = line.split()
   for w in word:
      if len(w)<4:
        print(w, end=' ') 
   file.close()
DISPLAYWORDS()

#Q3.1
def count_letter():
    file = open(ASSETS_DIR + "poem.txt","r")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count+=1
    print(count)
    file.close()

count_letter()

#Q3.2
def count_words():
    file = open(ASSETS_DIR + "poem.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word == 'this' or word =='these':
            count+=1
    print(count)
    file.close()

count_words()

#Q4.1
def count_hash():
    file = open(ASSETS_DIR + "poem.txt","r")
    data = file.read()
    for letter in data:
        print(letter, end="#")

    file.close()

count_hash()

#Q4.2
def JTOI():
    file = open(ASSETS_DIR + "poem.txt","r")
    data = file.read()
    for letter in data:
        if letter == 'J' :
            print("I",end="")
        else:
            print(letter,end="")

    file.close()

JTOI()