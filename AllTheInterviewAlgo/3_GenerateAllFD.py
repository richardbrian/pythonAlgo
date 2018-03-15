from itertools import permutations

def singleFD(fdHosts):
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

def getAllFdSolutions(faultDomainCombinations):

    allSolutions = []
    for eachNumber in faultDomainCombinations:
       allSolutions.extend(singleFD(eachNumber))

    megaPermute = permutations(allSolutions, len(faultDomainCombinations))
    finalSum = sum(minimumFdCombination)

    dedupeDict = {}
    finalAllSolutions = []
    for eachSolution in megaPermute:
        mergedL = mergeLists(eachSolution)
        if finalSum == sum(mergedL):
            if str(sorted(mergedL)) in dedupeDict:
                continue
            dedupeDict[str(sorted(mergedL))] = 0
            finalAllSolutions.append(mergedL)
            print(mergedL)
    print("TotalSolutions", len(finalAllSolutions))
# As we supported UFT=1   minimum fault domains we need to satisfy any policy are 3
# Each fault domain depending on policy we may support 'n' numbers minimum nodes.
# UFT=1 LFT=1 RAID1   Needs 3 fault domains with 3 nodes each. (3,3,3)
# UFT1 LFT2 RAID6  Needs  3 fault domains with minimum of 6 nodes each. (6,6,6)
minimumFdCombination = (6, 6, 6)
getAllFdSolutions(minimumFdCombination)