#!/usr/bin/python
# -*- coding=utf-8 -*-
#Usage: Syntax Parser, Homework of Principle of compiler.
#Author:fanTasy shAo

import tokenize, StringIO
import re
#设置全局变量
tokens = None
cur_tok = None
output = open('output.txt', 'w')
#扫描读入的字符串
def scan(text):
    g = tokenize.generate_tokens(
        StringIO.StringIO(text).readline)
    return ((v[0], v[1]) for v in g)
#获取token
def get_token():
    global tokens, cur_tok
    cur_tok = tokens.next()
    return cur_tok

def match(type, val = ''):
    global tokens, cur_tok
    t, v = cur_tok
    if t == type or t == tokenize.OP and v == val:
        get_token()
    else:
        raise

def expr():
    global cur_tok
    tmp = term()
    t, v = cur_tok
    while v == '+' or v == '-':
        match(tokenize.OP)
        rhs = term()
        e = str(tmp) + str(v) + str(rhs)
        tmp = eval(e)
        #print e, '=', tmp
        output.write(e + '=' + str(tmp) + '\n')
        t, v = cur_tok
    return tmp

def term():
    global cur_tok
    tmp = factor()
    t, v = cur_tok
    while v == '*' or v == '/':
        match(tokenize.OP)
        rhs = factor()
        e = str(tmp) + str(v) + str(rhs)
        tmp = eval(e)
        #print e, '=', tmp
        output.write(e + '=' + str(tmp) + '\n')
        t, v = cur_tok
    return tmp

def factor():
    global cur_tok
    t, v = cur_tok
    if t == tokenize.NUMBER:
        match(tokenize.NUMBER)
        return int(v)
    elif v == '(':
        match(tokenize.OP, '(')
        tmp = expr()
        match(tokenize.OP, ')')
        return tmp
    else:
        raise

if __name__ == '__main__':
    reduce_lin_regex = re.compile(r"(\\[\t\r]*\n)")
    inputFile = open('input.txt', 'r')
    text = ""
    #从文件中读入运算式
    text = reduce_lin_regex.sub(" ", inputFile.readline())
    tokens = scan(text)
    get_token()
    res = expr()
    print text, '=', res
    output.write( text + '=' + str(res) + '\n')


    
