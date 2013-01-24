#!/usr/bin/python
#Filename: mergeFile.py
#Usage: merge all the lines in test1 and test2

file1 = open('test1.txt', 'r')
file2 = open('test2.txt', 'r')
  
lines1 = file1.readlines()
lines2 = file2.readlines()
   
list1 = []
list2 = []
    
count = 0
     
for i in lines1:
    newLine = i.split(',')
    newLine = [int(p) for p in newLine]
    list1.append(newLine)
    print list1
                     
for i in lines2:
    newLine = int(i)
    list1[count].append(newLine)
    count += 1
                                  
with open('result.txt', 'w') as f:
    f.writelines(str(list1))
    f.close()
