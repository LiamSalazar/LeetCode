def findShortestCycle(n, edges):
    # Global variables declaration
    firstisCycle = True
    secondisCycle = True
    firstCycle = []
    secondCycle = []
    infirstCycle = []
    insecondCycle = []
    firstCycle.append(edges[0])
    infirstCycle.append(edges[0][1])
    # First Cycle Division
    for list in edges[1:]:
        if list[0] in infirstCycle:
            firstCycle.append(list)
            infirstCycle.append(list[1])
        if firstCycle[0][0] == list[1]: 
            break
    # Second Cycle Division
    excludedElements = [elemento for elemento in edges if elemento not in firstCycle]
    insecondCycle = []
    lenExcluded = len(excludedElements)
    if lenExcluded > 1:
        secondCycle.append(excludedElements[0])
        insecondCycle.append(excludedElements[0][1])
        for list in excludedElements[1:]:
            if list[0] in insecondCycle:
                secondCycle.append(list)
                insecondCycle.append(list[1])
            if secondCycle[0][0] == list[1]: 
                break
    # Length declaration
    len1 = len(firstCycle)
    len2 = len(secondCycle)
    print(firstCycle)
    print(secondCycle)
    #Not a cycle detection
    if len1 == 1 or len1 == 0: firstisCycle = False
    elif firstCycle[0][0] != firstCycle [len1-1][1]: firstisCycle == False
    if len2 == 1 or len2 == 0: secondisCycle = False
    elif secondCycle[0][0] != secondCycle [len2-1][1]: secondisCycle == False
    # Minor path
    if firstisCycle == False and secondisCycle == False:
        result = -1
    else:
        if firstisCycle == True and secondisCycle == True:
            if len1 > len2: result = len2
            else: result = len1
        else:
            if firstisCycle == True and secondisCycle == False:
                result = len1
            elif firstisCycle == False and secondisCycle == True:
                result = len2
    print(result)
    return result

# Test
n = 7
edges = [[4,1],[5,1],[3,2],[5,0],[4,0],[3,0],[2,1]]
findShortestCycle(n, edges)


