'''
15-110 Homework 4
Name: Riya Malhotra
Andrew ID: riyamalh
'''

'''
#1 - getLeftmost(t)
Parameters: binary tree holding values
Returns: value
'''
def getLeftmost(t):
    while t["left"] != None:
        t = t["left"]
    return t["contents"]


'''
#2 - getInitialTeams(bracket)
Parameters: binary tree holding strings
Returns: list of strings
'''

def getInitialTeams(bracket):
    result = []
    if bracket == None:
        return []
    if bracket["left"] == None and bracket["right"] == None:
        return [bracket["contents"]]
    if bracket["left"] != None:
        result += getInitialTeams(bracket["left"])
    if bracket["right"] != None:
        result += getInitialTeams(bracket["right"])
    return result

'''
#3 - largestEdge(g)
Parameters: weighted graph holding strings
Returns: list holding strings
'''

def largestEdge(g):
    maxWeight = 0
    egde = []
    for node in g:
        for element in g[node]:
            neighbor = element[0]
            weight = element[1]
            if weight > maxWeight:
                maxWeight = weight
                edge = [node, neighbor]
    return edge
    

'''
#4 - getPrereqs(g, course)
Parameters: directed graph of strings, string
Returns: list of strings
'''

def getPrereqs(g, course):
    prereq = []
    for node in g:
        for neighbor in g[node]:
            if course == neighbor:
                prereq.append(node)
    return prereq


################################################################################
#Test Functions 

def testGetLeftmost():
    print("Testing getLeftmost()...", end="")
    t1 = { "contents" : "A",
           "left" :  { "contents" : "B",
                       "left" :  { "contents" : "D",
                                   "left"  : None,
                                   "right" : None },
                       "right" : None },
           "right" : { "contents" : "C",
                       "left" :  { "contents" : "E",
                                   "left" :  { "contents" : "G",
                                               "left"  : None,
                                               "right" : None },
                                   "right" : { "contents" : "H",
                                               "left"  : None,
                                               "right" : None } },
                       "right" : { "contents" : "F",
                                   "left"  : None,
                                   "right" : None } } }
    assert(getLeftmost(t1) == "D")
    t2 = { "contents" : 10,
           "left" :  { "contents" : 25,
                       "left" :  { "contents" : 37,
                                   "left"  : { "contents" : 30,
                                               "left"  : None,
                                               "right" : None },
                                   "right" : { "contents" : 65,
                                               "left"  : None,
                                               "right" : None } },
                       "right" : { "contents" : 8,
                                   "left"  : { "contents" : 99,
                                               "left"  : None,
                                               "right" : None },
                                   "right" : { "contents" : 23,
                                               "left"  : None,
                                               "right" : None } } },
           "right" : { "contents" : 100,
                       "left" :  { "contents" : 72,
                                   "left" :  { "contents" : 3,
                                               "left"  : None,
                                               "right" : None },
                                   "right" : { "contents" : 89,
                                               "left"  : None,
                                               "right" : None } },
                       "right" : { "contents" : 42,
                                   "left"  : { "contents" : 12,
                                               "left"  : None,
                                               "right" : None },
                                   "right" : { "contents" : 50,
                                               "left"  : None,
                                               "right" : None } } } }
    assert(getLeftmost(t2) == 30)
    t3 = { "contents" : "alpha",
           "left" :  { "contents" : "beta",
                       "left" :  { "contents" : "gamma",
                                   "left"  : { "contents" : "delta",
                                               "left"  : None,
                                               "right" : None },
                                   "right" : None},
                       "right" : None },
           "right" : None }
    assert(getLeftmost(t3) == "delta")
    t4 = { "contents" : 1,
           "left" :  { "contents" : 2,
                       "left" :  None,
                       "right" : None },
           "right" : { "contents" : 3,
                       "left" :  None,
                       "right" : None } }
    assert(getLeftmost(t4) == 2)
    t5 = { "contents" : "foo",
           "left" :  None,
           "right" : None }
    assert(getLeftmost(t5) == "foo")
    print("... done!")

def testGetInitialTeams():
    print("Testing getInitialTeams()...", end="")
    # An order of teams is not specified, so we'll
    # sort your result before checking it
    t1 = { "contents" : "United States",
           "left"  : { "contents" : "United States",
                       "left"  : { "contents" : "England",
                                   "left"  : None,
                                   "right" : None
                                 },
                       "right" : { "contents" : "United States",
                                   "left"  : None,
                                   "right" : None
                                 }
                     },
            "right" : { "contents" : "Netherlands",
                        "left"  : { "contents" : "Netherlands",
                                    "left"  : None,
                                    "right" : None
                                  },
                        "right" : { "contents" : "Sweden",
                                    "left"  : None,
                                    "right" : None
                                  }
                     }
         }
    assert(sorted(getInitialTeams(t1)) == [ "England", "Netherlands", "Sweden", "United States" ])
    t2 = { "contents" : "CMU",
           "left"  : { "contents" : "CMU",
                       "left"  : None,
                       "right" : None
                     },
            "right" : { "contents" : "MIT",
                        "left"  : None,
                        "right" : None
                     }
         }
    assert(sorted(getInitialTeams(t2)) == [ "CMU", "MIT" ])
    t3 = { "contents" : "Kansas City",
           "left"  : { "contents" : "Kansas City",
                       "left"  : { "contents" : "Tennessee",
                                   "left"  : { "contents" : "Tennessee",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "contents" : "Baltimore",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 },
                       "right" : { "contents" : "Kansas City",
                                   "left"  : { "contents" : "Houston",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "contents" : "Kansas City",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 }
                     },
            "right" : { "contents" : "San Francisco",
                        "left"  : { "contents" : "San Francisco",
                                    "left"  : { "contents" : "Minnesota",
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "contents" : "San Francisco",
                                               "left"  : None,
                                               "right" : None
                                             }
                                  },
                        "right" : { "contents" : "Green Bay",
                                    "left"  : { "contents" : "Seattle",
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "contents" : "Green Bay",
                                               "left"  : None,
                                               "right" : None
                                             }
                                  }
                     }
         }
    assert(sorted(getInitialTeams(t3)) == [ "Baltimore", "Green Bay", "Houston", "Kansas City", "Minnesota", "San Francisco", "Seattle", "Tennessee" ])
    t4 = { "contents" : "Five Guys",
           "left"  : { "contents" : "Five Guys",
                       "left"  : { "contents" : "Five Guys",
                                   "left"  : None,
                                   "right" : None
                                 },
                       "right" : { "contents" : "Shake Shack",
                                   "left"  : { "contents" : "Steak 'n Shake",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "contents" : "Shake Shack",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 }
                     },
            "right" : { "contents" : "Culver's",
                        "left"  : { "contents" : "In-n-Out",
                                    "left"  : None,
                                    "right" : None
                                  },
                        "right" : { "contents" : "Culver's",
                                    "left"  : None,
                                    "right" : None
                                  }
                     }
         }
    assert(sorted(getInitialTeams(t4)) == [ "Culver's", "Five Guys", "In-n-Out", "Shake Shack", "Steak 'n Shake" ])
    t5 = { "contents" : "Stella",
           "left"  : None,
           "right" : None
         }
    assert(getInitialTeams(t5) == [ "Stella" ])
    print("... done!")

def testLargestEdge():
    print("Testing largestEdge()...", end="")
    g1 = { "A" : [ [ "B", 10 ], [ "C",  2 ], [ "F", 25 ] ],
           "B" : [ [ "A", 10 ], [ "D", 42 ] ],
           "C" : [ [ "A",  2 ], [ "E", 30 ] ],
           "D" : [ [ "B", 42 ] ],
           "E" : [ [ "C", 30 ], [ "F",  9 ] ],
           "F" : [ [ "A", 25 ], [ "E",  9 ] ],
           "G" : [ ] }
    assert(sorted(largestEdge(g1)) == [ "B", "D" ])
    g2 = { "A" : [ [ "B", 10 ], [ "C",  2 ], [ "F", 25 ] ],
           "B" : [ [ "A", 10 ], [ "D", 42 ] ],
           "C" : [ [ "A",  2 ], [ "E", 30 ] ],
           "D" : [ [ "B", 42 ] ],
           "E" : [ [ "C", 30 ], [ "F",  99 ] ], # one edge changed
           "F" : [ [ "A", 25 ], [ "E",  99 ] ],
           "G" : [ ] }
    assert(sorted(largestEdge(g2)) == [ "E", "F" ])
    g3 = { "A" : [ [ "B", 99 ], [ "C",  2 ], [ "F", 25 ] ], # one edge changed
           "B" : [ [ "A", 99 ], [ "D", 42 ] ],
           "C" : [ [ "A",  2 ], [ "E", 30 ] ],
           "D" : [ [ "B", 42 ] ],
           "E" : [ [ "C", 30 ], [ "F",   9 ] ],
           "F" : [ [ "A", 25 ], [ "E",   9 ] ],
           "G" : [ ] }
    assert(sorted(largestEdge(g3)) == [ "A", "B" ])
    g4 = { "A" : [ [ "B", 10 ], [ "C",  2 ], [ "D", 21 ], [ "E",  8 ], [ "F", 25 ], [ "G", 80 ] ],
           "B" : [ [ "A", 10 ], [ "C", 50 ], [ "D", 42 ], [ "E", 49 ], [ "F", 13 ], [ "G", 75 ] ],
           "C" : [ [ "A",  2 ], [ "B", 50 ], [ "D", 67 ], [ "E", 30 ], [ "F", 18 ], [ "G", 29 ] ],
           "D" : [ [ "A", 21 ], [ "B", 42 ], [ "C", 67 ], [ "E", 44 ], [ "F", 36 ], [ "G", 71 ] ],
           "E" : [ [ "A",  8 ], [ "B", 49 ], [ "C", 30 ], [ "D", 44 ], [ "F",  9 ], [ "G", 43 ] ],
           "F" : [ [ "A", 25 ], [ "B", 13 ], [ "C", 18 ], [ "D", 36 ], [ "E",  9 ], [ "G",  5 ] ],
           "G" : [ [ "A", 80 ], [ "B", 75 ], [ "C", 29 ], [ "D", 71 ], [ "E", 43 ], [ "F",  5 ] ] }
    assert(sorted(largestEdge(g4)) == [ "A", "G" ])
    g5 = { "A" : [ [ "B", 10 ], [ "C", 42 ] ],
           "B" : [ [ "A", 10 ], [ "D",  2 ] ],
           "C" : [ [ "A", 42 ] ],
           "D" : [ [ "B",  2 ] ] }
    assert(sorted(largestEdge(g5)) == [ "A", "C" ])
    g6 = { "A" : [ ],
           "B" : [ [ "C", 10 ] ],
           "C" : [ [ "B", 10 ] ],
           "D" : [ ] }
    assert(sorted(largestEdge(g6)) == [ "B", "C" ])
    print("... done!")

def testGetPrereqs():
    print("Testing getPrereqs()...", end="")
    g = { "110" : [],
        "112" : ["122", "150"],
        "122" : ["213", "210", "251", "281"],
        "150" : ["210", "251"],
        "151" : ["150", "251", "281"],
        "210" : [],
        "213" : [],
        "251" : [],
        "281" : [] }
    # An order of courses is not specified, so we'll
    # sort your result before checking it
    assert(getPrereqs(g, "210") != None)
    assert(sorted(getPrereqs(g, "210")) == ["122", "150"])
    assert(sorted(getPrereqs(g, "251")) == ["122", "150", "151"])
    assert(getPrereqs(g, "213") == ["122"])
    assert(getPrereqs(g, "150") == ["112", "151"])
    assert(getPrereqs(g, "112") == [])
    assert(getPrereqs(g, "110") == [])

    g2 = { "Differential and Integral Calculus" : ["Integration and Approximation",
                                                   "Multivariate Analysis"],
           "Integration and Approximation" : ["Calculus in Three Dimensions",
                                              "Differential Equations",
                                              "Operations Research I"],
           "Concepts of Mathematics" : ["Discrete Mathematics"],
           "Discrete Mathematics" : ["Operations Research I"],
           "Matrices and Linear Transformations" : ["Operations Research I"],
           "Multivariate Analysis" : [],
           "Calculus in Three Dimensions" : [],
           "Differential Equations" : [],
           "Operations Research I" : [] }
    assert(sorted(getPrereqs(g2, "Operations Research I")) == ["Discrete Mathematics", "Integration and Approximation", "Matrices and Linear Transformations"])
    assert(getPrereqs(g2, "Discrete Mathematics") == ["Concepts of Mathematics"])
    assert(getPrereqs(g2, "Matrices and Linear Transformations") == [])
    print("... done!")

def testAll():
    testGetLeftmost()
    testGetInitialTeams()
    testLargestEdge()
    testGetPrereqs()

testAll()