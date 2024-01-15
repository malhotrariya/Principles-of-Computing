'''
15-110 Homework 3
Name: Riya Malhotra
Andrew ID: riyamalh
'''
#import libraries
import tkinter as tk

################################################################################

'''
#1 - onlyPositive(lst)
Parameters: 2D list of numbers
Returns: list of numbers
'''

def onlyPositive(lst):
    result = []
    for sublist in lst:
        for num in sublist:
            if num > 0:
                result.append(num)
    return result
    

'''
#2 - addToEach(lst, s)
Parameters: list of strings, str
Returns: None
'''

def addToEach(lst, s):
    for i in range(len(lst)):
        lst[i] = lst[i] + s
    return None

'''
#3 - recursiveLongestString(lst)
Parameters: list of strings
Returns: str
'''

def recursiveLongestString(lst):
    if len(lst) == 1:
        return lst[0]
    longestString = recursiveLongestString(lst[1:])
    if len(lst[0]) > len(longestString):
        return lst[0]
    else:
        return longestString

'''
#4 - generateBubbles(canvas, bubbleList)
Parameters: Tkinter canvas, list of dicts mapping strs to values
Returns: None
'''

def generateBubbles(canvas, bubbleList):
    for dimension in bubbleList:
        left = dimension["left"]
        top = dimension["top"]
        size = dimension["size"]
        color = dimension["color"]
        
        canvas.create_oval(left, top, left + size, top + size, fill=color)
       
'''
#5 - getBookByAuthor(bookInfo, author)
Parameters: dict mapping strs to strs, str
Returns: str
'''

def getBookByAuthor(bookInfo, author):
    names = list(bookInfo.keys())
    authors = list(bookInfo.values())
    for i in range(len(authors)):
        if authors[i] == author:
            return names[i]
    return None


'''
#6 - makeIMDB(actorList, movieList)
Parameters: list of strs, list of strs
Returns: dict mapping strs to strs
'''

def makeIMDB(actorList, movieList):
    result = {}
    for i in range(len(actorList)):
        if actorList[i] not in result:
            result[actorList[i]] = movieList[i]
    return result


################################################################################
#Test Functions

def testOnlyPositive():
    print("Testing onlyPositive()...", end="")
    assert(onlyPositive([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6])
    assert(onlyPositive([[0, 1, 2], [-2, -1, 0], [10, 9, -9]]) == [1, 2, 10, 9])
    assert(onlyPositive([[-4, -3], [-2, -1]]) == [ ])
    assert(onlyPositive([[3, 4, 5]]) == [3, 4, 5])
    assert(onlyPositive([[-4], [3], [5]]) == [3, 5])
    assert(onlyPositive([[-1, 2], [-3, 4], [-5, 6]]) == [2, 4, 6])
    assert(onlyPositive([[1, 5, -3, 7, 9, -23, -45, 67]]) == [1, 5, 7, 9, 67])
    assert(onlyPositive([[-5], [-4], [-3], [-2], [-1]]) == [ ])
    assert(onlyPositive([ [0], [0] ]) == [ ])
    print("... done!")

def testAddToEach():
    print("Testing addToEach()...", end="")
    lst1 = ["how", "are", "you"]
    assert(addToEach(lst1, "yah") == None) # addToEach is destructive- change the parameter instead of returning
    assert(lst1 == ["howyah", "areyah", "youyah"])
    
    lst2 = ["1", "2", "3"]
    assert(addToEach(lst2, "2") == None)
    assert(lst2 == ["12", "22", "32"])

    lst3 = ["a", "bc", "dee", "f", "gh"]
    assert(addToEach(lst3, "qr") == None)
    assert(lst3 == ["aqr", "bcqr", "deeqr", "fqr", "ghqr"])

    lst4 = ["yz"]
    assert(addToEach(lst4, "abc") == None)
    assert(lst4 == ["yzabc"])

    lst5 = []
    assert(addToEach(lst5, "lol") == None)
    assert(lst5 == [])
    print("... done!")

def testRecursiveLongestString():
    print("Testing recursiveLongestString()...", end="")
    assert(recursiveLongestString(["a", "bb", "ccc"]) == "ccc")
    assert(recursiveLongestString(["hi", "its", "fantastic", "here"]) == "fantastic")
    assert(recursiveLongestString(["tremendously", "excited", "for", "today"]) == "tremendously")
    assert(recursiveLongestString(["Carnegie", "Mellon", "University"]) == "University")
    assert(recursiveLongestString(["when", "you", "wish", "upon", "a", "star", "doesn't", "matter", "who", "you", "are"]) == "doesn't")
    assert(recursiveLongestString(["computer", "science"]) == "computer")
    assert(recursiveLongestString(["python", "program"]) == "program")
    assert(recursiveLongestString(["programming"]) == "programming")
    print("... done!")

def makeNBubbles(n):
    import random
    bubbles = []
    for i in range(n):
        size = random.randint(1, 200)
        top = random.randint(0, 400 - size)
        left = random.randint(0, 400 - size)
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "pink"])
        bubbles.append({ "left" : left, "top" : top, "size" : size, "color" : color })
    return bubbles

def runGenerateBubbles():
    print("Testing generateBubbles()... check the screen!")
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    bubbleList1 = [ {"left" : 150, "top" : 150, "size" : 100, "color" : "green" } ]
    generateBubbles(canvas, bubbleList1)
    root.mainloop()

    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    bubbleList2 = [
        {'left': 317, 'top': 269, 'size': 45, 'color': 'red'   },
        {'left': 118, 'top':  27, 'size': 90, 'color': 'orange'},
        {'left': 101, 'top': 321, 'size': 65, 'color': 'yellow'},
        {'left': 231, 'top': 219, 'size': 25, 'color': 'pink'  },
        {'left':  50, 'top':  12, 'size': 20, 'color': 'blue'  }]
    generateBubbles(canvas, bubbleList2)
    root.mainloop()

    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    randomBubbles = makeNBubbles(10)
    generateBubbles(canvas, randomBubbles)
    root.mainloop()
    print("... generateBubbles() closed successfully.")

def testGetBookByAuthor():
    print("Testing getBookByAuthor()...", end="")
    assert(getBookByAuthor({ "The Hobbit" : "JRR Tolkein", "Harry Potter and the Sorcerer's Stone" : "JK Rowling", "A Game of Thrones" : "George RR Martin" }, "JK Rowling") == "Harry Potter and the Sorcerer's Stone")
    assert(getBookByAuthor({ "A Wrinkle in Time" : "Madeline L'Engle", "The Golden Compass" : "Phillip Pullman" }, "Madeline L'Engle") == "A Wrinkle in Time")
    assert(getBookByAuthor({ "The Chronicles of Chrestomanci" : "Diana Wynne Jones", "The Name of the Wind" : "Patrick Rothfuss", "Skyward" : "Brandon Sanderson", "The Fifth Season" : "N.K. Jemisin" }, "N.K. Jemisin") == "The Fifth Season")
    assert(getBookByAuthor({ "A Natural History of Dragons" : "Marie Brennan"}, "Marie Brennan") == "A Natural History of Dragons")
    assert(getBookByAuthor({ "The Chronicles of Chrestomanci" : "Diana Wynne Jones", "The Name of the Wind" : "Patrick Rothfuss", "Skyward" : "Brandon Sanderson", "The Fifth Season" : "N.K. Jemisin" }, "JRR Tolkein") == None)
    assert(getBookByAuthor({ }, "Brandon Sanderson") == None)
    print("... done!")

def testMakeIMDB():
    print("Testing makeIMDB()...", end="")
    assert(makeIMDB(["Ni Ni", "Sofia Vergara", "Ni Ni"], ["Suddenly Seventeen", "Hot Pursuit", "Love Will Tear Us Apart"]) == { "Ni Ni" : "Suddenly Seventeen", "Sofia Vergara" : "Hot Pursuit" })
    assert(makeIMDB(["Ni Ni", "Chen Kun", "Sofia Vergara", "Halle Berry"], ["The flowers of War", "Beautiful Accident", "Modern Family", "Robots"]) == { "Ni Ni" : "The flowers of War", "Chen Kun" : "Beautiful Accident", "Sofia Vergara" : "Modern Family", "Halle Berry" : "Robots" })
    assert(makeIMDB(["Will Smith", "Will Smith", "Will Smith"], ["Man in Black 3", "Man in Black 2", "Man in Black 1"]) == { "Will Smith" : "Man in Black 3" })
    assert(makeIMDB(["Keanu Reeves"], ["The Matrix"]) == { "Keanu Reeves" : "The Matrix" })
    assert(makeIMDB(["Ni Ni", "Ni Ni", "Sofia Vergara"], ["Suddenly Seventeen", "Love Will Tear Us Apart", "Hot Pursuit"]) == { "Ni Ni" : "Suddenly Seventeen", "Sofia Vergara" : "Hot Pursuit" })
    assert(makeIMDB([ ], [ ]) == { })
    print("... done!")

def testAll():
    testOnlyPositive()
    testAddToEach()
    testRecursiveLongestString()
    runGenerateBubbles()
    testGetBookByAuthor()
    testMakeIMDB()

testAll()
