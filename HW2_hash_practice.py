# -*- coding: utf-8 -*-
"""Hash

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bKVNP_Xqi7mnL6jzmWRzd_R3EOrosvF_
"""

with open('hw2_data.txt', 'r') as file:
  n = 0
  dictionary = {}
  for string in file:
    string = string.strip()
    if string in dictionary:
      dictionary[string] += 1
    else:
      dictionary[string] = 1
      n += 1
print(n , "different strings in the file")
print(dictionary)