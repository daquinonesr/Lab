#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:50:50 2019

@author: diegoquinones
"""

import numpy as np
import math
import time

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
# Implementation of hash tables with chaining using strings
#All of this code belongs to hash table

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*255 + ord(c))% n
    return r

def EmptyPer(H):
    counter=0
    for i in H.item:
        if i ==[]:
            counter=+1
    return counter

def Similarity(H,file):
    print('Reading word file to determine similarities ')
    print()
    print('Word similarities found:')
    print()
    for i in file:
        word=i.split(',')
        word[1]=word[1].replace('\n',' ')
        a=FindC(H,word[0])
        b=FindC(H,word[1])
        print('Similarity', word,'=',round(np.sum(a*b)/(math.sqrt(np.sum(a*a)))*math.sqrt(np.sum(b*b))))

def HashBuilder(v):
    print('Building hash table with chaining',end=' ')
    H1=HashTableC(23)
    print('Initial Size: ', len(H1.item)) 
    for i in v:
        line = i
        letters=line.split(" ")
        word=letters[0]
        embed = np.empty([50], dtype=float)
        for j in range(len(letters)):
            embed[j]=letters[j]
        InsertC(H1,word,embed)
        H1.num_items=H1.num_items+1
    EmptyLists=((EmptyPer(H1))/len(H1.item) )*100
    deviation=SDev(H1)
    print('Final Table Size: ',len(H1.item))
    print('Percentage of empty lists: ',EmptyLists,' %')
    print('Standard deviation of the lengths of the lists: ',deviation)
    return H1
    
#doubles size of hash table
def ExpandHash(H):
    #creates longer hash
    H1= HashTableC((len(H.item)*2)+1)
    
    #inserts values to new hash
    for i in range(len(H.item)):
        for j in H.item[i]:
            InsertC(H1,j[0],j[1])
    return H1
    

def loadFactor(H):
    return H.num_items//len(H.items)


def SDev(H):
    a=0
    k=loadFactor(H)
    for i in H.item:
        a=a+ len(i)-k
    standard=((1/len(H.items)*a)/(len(H.items)))*100
    return standard
    
#All of this code belong to BST

def Tree(a):
    print('Building binary search tree')
    k=None
    nodeCounter=0
    for i in a:
        line=i
        text=line.split(" ")
        word = text[0]
        j= value(word)
        e=np.empty([50],dtype=float)
        for k in range(1,len(text)):
            e[k]=text[k]
        k=Insert(k,[j,word,e])
        nodeCounter+=1
    print('Number of nodes: ',nodeCounter)
    return k

def Insert(T,newItem):
    if T==None:
        T=BST(newItem)
    elif T.item[0]>newItem[0]:
        T.left=Insert(T.left,newItem)
    else:
        T.right=Insert(T.right,newItem)
    return T

def height(T):
    counter=0
    temp1=T
    temp2=T
    while temp1 is not None:
        counter=counter+1
        temp1=temp1.left
    counter=0
    while temp2 is not None:
        counter=counter+1
        temp2=temp2.right
    if temp1>temp2:
        return temp2
    return temp1

def value(w):
    num=[ord(c) for c in w]
    counter=0
    for i in num:
        counter=counter+1
    return counter

def wordfinder(T,k):
    temp=T
    while temp is not None:
        if temp.item[0]==value(k) and temp.item[1]==k:
            return temp.item
        elif temp.item[0]<value(k):
            temp=temp.right
        else:
            temp=temp.left
    return None

def similaritybst(T,file):
    print('Reading word file to determine similarities')
    print()
    print('Word similarities found: ')
    print()
    for words in file:
        words=words.split(',')
        words[1]=words[1].replace('\n',' ').replace()
        words2=wordfinder(T,words[0])
        words3=wordfinder(T,words[1])
        print('Similarity', words,'=',round(np.sum(words2*words3)/(math.sqrt(np.sum(words2*words2)))*math.sqrt(np.sum(words3*words3))))
    
    
#main method
userinput= input('Choose table implementation Type 1 for binary search tree or 2 for hash table with chaining')
file=open("glove.6B.50d.txt","r")
words=open("words.txt","r")
type(userinput)
if userinput=='2':
    print('Choice: ',2)
    HT=HashBuilder(file)
    Similarity(HT,words)
    
if userinput=='1':
    print('Choice: ',1)
    BS=Tree(file)
    similaritybst(BS,words)
    
    

    
    
    
    
    
    
    
    