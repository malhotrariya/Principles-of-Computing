'''
15-110 Homework 1
Name: Riya Malhotra
Andrew ID: riyamalh
'''
#import libraris

#Programming Basics 
''' #1 - Data Types '''
print("---1---")
a = int(15) #Assigning the integer 15 to the variable a
b = float(3.14) #Assigning the float 3.14 to the variable b
c = str(20) #Assigning the string "20" to the variable c
d = bool(True) #Assigning the boolean True to the variable d
e = 5 - 1.7 #Evaluating 5 minus 1.7
f = 8 < 5 #Checking whether 8 is less than 5
a = 45 #Reassigning the variable a to hold the value 45
g = c + "21"  #Concatenate c and "21"

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

''' #2 - Printing '''
print("---2---")
prof = "Kelly" #Assigning the string Kelly to prof
ta = "Benjamin" #Assigning a string course 15-110 TA's name to ta
print("Hello", prof, "and", ta) 

''' #3 - Using Function Calls '''
print("---3---")
import random
import math
x = random.randint(1, 360) #Generating a random integer between [1, 360] 
r = math.radians(x)
print(x, "degrees is", r, "radians")

''' #4 - Libraries (Graphics) '''
print("---4---")

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.configure(bd=0, highlightthickness=0)
canvas.pack()
canvas.create_rectangle(60, 80, 100, 200, fill = 'red')
canvas.create_rectangle(220, 80, 260, 200, fill = 'red')
canvas.create_rectangle(100, 100, 220, 130, fill = 'blue')
canvas.create_rectangle(100, 150, 220, 180, fill = 'blue')

# draw fence here


root.mainloop()


''' #5 - Defining Functions '''
print("---5---")
def slope(x1, y1, x2, y2):
    diffy = y2 - y1
    diffx = x2 - x1
    m = (diffy/diffx)
    return m

print(slope(2, 4, 5, 6))
