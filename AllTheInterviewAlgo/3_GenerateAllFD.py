from itertools import permutations

def singleFD(fdHosts):
    pft=1
    sft=1
    policyType = 'P'
    # Generate all  possible numbers to create the sum
    result = []
    for i in range(1,fdHosts+1):
        res = int(fdHosts/i)
        for j in range (1,res+1):
            result.append(i)

    allSolutions = []
    uniqueSolutions = {}
    for i in range(1,fdHosts+1):
        permutation1 = permutations(result,i)
        for  solution in permutation1:
            if sum(solution) == fdHosts:
               if not uniqueSolutions:
                   uniqueSolutions[str(sorted(solution))] = 0
               elif str(sorted(solution)) in uniqueSolutions:
                   continue
               uniqueSolutions[str(sorted(solution))] = 0
               allSolutions.append(sorted(solution))
    return allSolutions

def mergeLists(inputList):
    mergedL = []
    for eachList in inputList:
        mergedL += eachList
    return mergedL

minimumFdCombination= (6,6,6)
allSolutions = []
allSolutions.extend(singleFD(minimumFdCombination[0]))
allSolutions.extend(singleFD(minimumFdCombination[1]))
allSolutions.extend(singleFD(minimumFdCombination[2]))
megaPermute = permutations(allSolutions,3)
finalSum = sum(minimumFdCombination)

dedupeDict = {}
i =1
finalAllSolutions = []
for eachSolution in megaPermute:
    mergedL = mergeLists(eachSolution)
    if finalSum == sum(mergedL):
        if str(sorted(mergedL)) in dedupeDict:
            continue
        dedupeDict[str(sorted(mergedL))] = 0
        finalAllSolutions.extend(mergedL)
        print(mergedL)
        i += 1
print("Total solutions=", i)
