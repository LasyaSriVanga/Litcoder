# Problem Statement:
# You are developing a text editor that allows users to perform various operations on the text using the "CustomStack" class. The class supports the following operations:
# insert(value): Inserts a string of characters at the current cursor position in the text.
# delete(value): Deletes the last value characters from the text starting from the current cursor position.
# get(value): Retrieves the character at index value from the text and displays it.
# undo(): Reverts the last executed command on the text.

# Each command is represented by a string in the following format:
# 1.Command 1: '1 value' - Inserts the string value at the current cursor position in the text. 
# 2.Command 2: '2 value' - Deletes the last value characters from the text starting from the current cursor position. 
# 3.Command 3: '3 value' - Retrieves the character at index value from the text and displays it. 
# 4.Command 4: '4' - Reverts the last executed command on the text.

# Consider a scenario where you have a text editor with a "CustomStack" class that implements the required operations. Assume the initial text is empty.

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Exercise-1 input: 1 abc,3 3,2 2,3 1
# Here 1 abc -> command and input text 3 3 -> command and index of the stack 
# Output: c a

# Exercise-2 Input: 1 zxy,3 3,2 2,1 def,3 2
# Output: y d

import sys
class Editor:
    def __init__(self):
        self.arr = [""]
    def insert(self,string):
        self.arr.append(self.arr[-1]+string)
    def delete(self,k):
        if len(self.arr) < 2:
            retuen
        elif len(self.arr[-1]) < k:
            self.arr.append("")
        else:
            self.arr.append(self.arr[-1][:-k])
    def get(self,k):
        if len(self.arr) < 2:
            return
        elif len(self.arr[-1]) < k:
            return
        else:
            print(self.arr[-1][k-1])
    def undo(self):
        if len(self.arr) > 1:
            self.arr.pop()
        else:
            return
        
editor = Editor()
operations = input().split(",")
for operation in operations:
    operator = operation.split(" ")[0]
    if operator == "1":
        editor.insert(operation.split(" ")[1])
    elif operator == "2":
        editor.delete(int(operation.split(" ")[1]))
    elif operator == "3":
        editor.get(int(operation.split(" ")[1]))
    elif operator == "4":
        editor.undo()