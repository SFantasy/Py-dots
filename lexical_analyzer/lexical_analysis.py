#!/usr/bin/python
# -*- coding=utf-8 -*-
#Filename:lexical_analysis.py
#Usage: Lexical analysis, Homework of the Principle of compiler.
#Author:fanTasy shAo

import re
#python 中的保留字
keywords = ('print', 'while', 'if', 'elif', 'else', 'import', 'def', 'global')
#分隔符
separators = ('(', ')', ':')
#操作符
operators = ('=', '>', '<', '>=', '<=', '*', '/', '+', '-')
text = ""

def preprocess():
    reduce_lin_regex = re.compile(r"(\\[\t\r]*\n)")
    i = 0
    global text
    #读取文件
    filename = "test.py"
    with open(filename) as in_file:
        for line in in_file:
            i += 1
            text += reduce_lin_regex.sub(" ",line)

def process():
    output = open("output.txt", 'w')
    #变量名 abc
    var_regex = re.compile(r"[a-zA-Z_]\w*")
    #字符串 "***"
    str_regex = re.compile(r'("((\\")|[^"])*")')
    #数字 123
    num_regex = re.compile(r"([0-9]+)")
    #逐行分析
    for line in text.split('\n'):
        line = line.strip('\t\r')
        words = line.split(' ')
        i = 0
        while 1:
            if i >= len(line):
                break
            if line[i].isspace():
                i += 1
                continue
            elif line[i].isalpha():
                #先判断是否为关键字，否，则为变量名
                temp = var_regex.search(line[i:]).group(0)
                if temp in keywords:
                    print "< " + temp + ", keywords >"
                    output.write("< " + temp + ", keywords >\n")
                else:
                    print "< " + temp + ",varName >"
                    output.write("< " + temp + ", varName >\n")
                i += len(temp)
                continue
            elif line[i] == '"':
                temp = str_regex.search(line[i:]).group(0)
                print "< " + temp + ", string >"
                output.write("< " + temp + ", string >\n")
                i += len(temp)
                continue
            elif line[i].isdigit():
                #识别数字
                temp = num_regex.search(line[i:]).group(0)
                print "< " + temp + ", number >"
                output.write("< " + temp + ", number >\n")
                i += len(temp)
                continue
            elif line[i] in separators:
                print "< " + line[i] + ", separator >"
                output.write("< " + temp + ", number >\n")
                i += 1
            else:
                #先从两个字符的操作符开始判断
                temp = line[i:i+2]
                if temp in operators:
                    print "< " + temp + ", operator >"
                    output.write("< " + temp + ", operator >\n")
                    i += 2
                #继而判断单个字符的操作符
                elif temp[0] in operators:
                    print "< " + temp[0] + ", operator >"
                    output.write("< " + temp[0] + ", operator >\n")
                    i += 1
                #既不是操作符，也不是关键字，也不是变量和字符串
                else:
                    print "< " + line[i:] + ", unknown >"
                    output.write("< " + line[i:] + ", unknown >\n")
                    break
                continue

preprocess()    
process()
