# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:34:40 2019

@author: Dimpoo
"""

import string
letters = string.ascii_letters
dict1={}
new_string = ""
new_file = open("substitution_cipher_text2.txt", "w")
for i in range(len(letters)):
    dict1[letters[i]] = letters[i-2]
    
with open("substitution_cipher_text1.txt") as file:
    while True:
        char = file.read(1)
        if char == "":
            print(new_string)
            print("EOF")
            break
        if char in letters:
            new_string += dict1[char]
        else:
            new_string += char
            
new_file.write(new_string)
new_file.close()