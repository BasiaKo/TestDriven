import math

def add(a,b, c=''):
#Adds two or three strings
    ret_val = a+b+c
    return ret_val

def upper(a):
#Converts a string into upper case
    ret_val = a.upper()
    return ret_val

def lower(a):
#Converts a string into lower case
    ret_val = a.lower()
    return ret_val

def length(a):
#resturn length of string
    ret_val = len(a)
    return ret_val

def islover(a):
#Returns True if all characters in the string are lower case
    if a=='':
        ret_val=True
    elif a!='':
        ret_val = str(a).islower()
    return ret_val
