'''
15-110 Homework 2
Name: Riya Malhotra
Andrew ID: riyamalh
'''
#import libraries
import tkinter

'''
#1 - drawIllusion(canvas)
Parameters: Tkinter canvas
Returns: None
'''

def drawIllusion(canvas):
    for margin in range(0,200,20):
        if margin % 40 == 0:
            color = "black"
        else:
            color = "white"
        canvas.create_rectangle(margin, margin, 400-margin, 400-margin, fill = color)


'''
#2 - partialProduct(n, x)
Parameters: int, int
Returns: int
'''

def partialProduct(n, x):
    product = 1
    for i in range(n, x+1):
        product = product * i
    return product

'''
#3 - printDiamond(n)
Parameters: int
Returns: None
'''

def printDiamond(n):
    for i in range(1, n + 1):
        sp = " " * (n - i)
        if i == 1:
            st = "11"
        else:
            st = str(i) + "*" * (2 * (i - 1)) + str(i)
        print(sp + st)


    for i in range(n - 1, 0, -1):
        sp = " " * (n - i)
        if i == 1:
            st = "11"
        else:
            st = str(i) + "*" * (2 * (i - 1)) + str(i)
        print(sp + st)


'''
#4 - printPrimeFactors(x)
Parameters: int
Returns: None

'''

def printPrimeFactors(x):
    for factor in range(2, x + 1):
        count = 0

        for count in range(x):
            if x % factor == 0:
                count= count + 1
                x //= factor
            else:
                break

        if count > 0:
            if count == 1:
                print(factor)
            else:
                print(factor,"**",count)
       

'''
#5 - repeatingPattern(canvas, numCells, cellSize, showGrid)
Parameters: Tkinter canvas, int, int, bool
Returns: None
'''

def repeatingPattern(canvas, numCells, cellSize, showGrid):
    pattern = 0

    for row in range(numCells):
        for col in range(numCells):
            x1 = col * cellSize
            y1 = row * cellSize
            x2 = x1 + cellSize
            y2 = y1 + cellSize

            if showGrid:
                canvas.create_rectangle(x1, y1, x2, y2, outline = 'black')

            canvas.create_oval(x1, y1, x2, y2, fill = 'yellow')
    
            if pattern % 2 == 0:
                
                canvas.create_line(x1, y1, x2, y2, fill = 'black')
            else:
                canvas.create_line(y2, x1, y1, x2, fill = 'black')

            pattern = 1 + pattern


'''
#6 - getSecretMessage(s, key)
Parameters: str, str
Returns: str
'''

def getSecretMessage(s, key):
    secretMessage = ""
    i = 0

    while i < len(s):
        if s[i] == key:
            secretMessage = secretMessage + s[i + 1]
            i = i + 2  
        else:
            i = i + 1

    return secretMessage

print(getSecretMessage("orupqcrzypqomqmhcyqpwhhqutqtxtqeyeqrpa","q"))



################################################################################

#Test Functions

def runDrawIllusion():
    print("Testing drawIllusion()... check the screen!")
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=400, height=400)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawIllusion(canvas)
    root.mainloop()
    print("... drawIllusion() closed successfully.")

def testPartialProduct():
    print("Testing partialProduct()...", end="")
    assert(partialProduct(1, 1) == 1)
    assert(partialProduct(1, 2) == 2)
    assert(partialProduct(1, 3) == 6)
    assert(partialProduct(3, 4) == 12)
    assert(partialProduct(3, 5) == 60)
    assert(partialProduct(2, 6) == 720)
    assert(partialProduct(7, 10) == 5040)
    assert(partialProduct(4, 10) == 604800)
    assert(partialProduct(10, 10) == 10)
    assert(partialProduct(0, 0) == 0)
    print("... done!")

def testPrintDiamond():
    print("Testing printDiamond()...")
    print("Diamond of size 1") # should just be '11'
    printDiamond(1)
    print("---")
    print("Diamond of size 2") # should be '11', then '2**2', then '11'
    printDiamond(2)
    print("---")
    print("Diamond of size 3")
    printDiamond(3)
    print("---")
    print("Diamond of size 4")
    printDiamond(4)
    print("---")
    print("Diamond of size 7")
    printDiamond(7)
    print("---")
    print("... check your output to see if it looks correct!")

def testPrintPrimeFactors():
    print("Testing printPrimeFactors()...")
    print("Factors of the number 70:")
    printPrimeFactors(70) # 2, 5, 7
    print("---")
    print("Factors of the number 12:")
    printPrimeFactors(12) # 2 ** 2, 3
    print("---")
    print("Factors of the number 16:")
    printPrimeFactors(16) # 2 ** 4
    print("---")
    print("Factors of the number 600:")
    printPrimeFactors(600) # 2 ** 3, 3, 5 ** 2
    print("---")
    print("Factors of the number 36:")
    printPrimeFactors(36) # 2 ** 2, 3 ** 2
    print("---")
    print("Factors of the number 3289:")
    printPrimeFactors(3289) # 11, 13, 23
    print("---")
    print("Factors of the number 17:")
    printPrimeFactors(17) # 17
    print("---")
    print("Factors of the number 2:")
    printPrimeFactors(2) # 2
    print("---")
    print("... check your output to see if it looks correct!")

def runRepeatingPattern():
    print("Testing repeatingPattern()... check the screen!")
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=400, height=400)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    repeatingPattern(canvas, 4, 100, True)
    root.mainloop()

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=400, height=400)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    repeatingPattern(canvas, 4, 100, False)
    root.mainloop()

    # Single cell
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=250, height=250)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    repeatingPattern(canvas, 1, 250, True)
    root.mainloop()

    # Lots of cells
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=500, height=500)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    repeatingPattern(canvas, 10, 50, False)
    root.mainloop()
    print("... repeatingPattern() closed successfully.")

def testGetSecretMessage():
    print("Testing getSecretMessage()...", end="")
    assert(getSecretMessage("orupqcrzypqomqmhcyqpwhhqutqtxtqeyeqrpa", "q") == "computer")
    assert(getSecretMessage("cowkscaoktbphakebakltvklmtkau", "k") == "stella")
    assert(getSecretMessage("xwuexoerxwdf", "x") == "wow")
    assert(getSecretMessage("faqfxwuexoerxw", "x") == "wow")
    assert(getSecretMessage("faqfxwuexoxwdf", "x") == "wow")
    assert(getSecretMessage("xwxoxw", "x") == "wow")
    assert(getSecretMessage("", "a") == "")
    print("... done!")

def testAll():
    runDrawIllusion()
    testPartialProduct()
    testPrintDiamond()
    testPrintPrimeFactors()
    runRepeatingPattern()
    testGetSecretMessage()

testAll()
