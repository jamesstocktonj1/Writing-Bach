#key finder functions
#James Stockton
#26/03/19

'''
    findSimular
     - keyArr - is the key to which you are comparing the inputed notes
     - testArr - is the inputed notes
     - returns: - array of simular notes


'''



CMaj =      [0, 2, 4, 5, 7, 9, 11]
CSMaj =     [1, 3, 5, 6, 8, 10, 0]
DMaj =      [2, 4, 6, 7, 9, 11, 1]
DSMaj =     [3, 5, 7, 8, 10, 0, 2]
EMaj =      [4, 6, 8, 9, 11, 1, 3]
FMaj =      [5, 7, 9, 10, 0, 2, 4]
FSMaj =     [6, 8, 10, 11, 1, 3, 5]
GMaj =      [7, 9, 11, 0, 2, 4, 6]
GSMaj =     [8, 10, 0, 1, 3, 5, 7]
AMaj =      [9, 11, 1, 2, 4, 6, 8]
ASMaj =     [10, 0, 2, 3, 5, 7, 9]
BMaj =      [11, 1, 3, 4, 6, 8, 10]

#melodic minors + risen seventh
CMin =      [0, 2, 3, 5, 7, 8, 10, 11]
CSMin =     [1, 3, 4, 6, 8, 9, 11, 0]
DMin =      [2, 4, 5, 7, 9, 10, 0, 1]
DSMin =     [3, 5, 6, 8, 10, 11, 1, 2]
EMin =      [4, 6, 7, 9, 11, 0, 2, 3]
FMin =      [5, 7, 8, 10, 0, 1, 3, 4]
FSMin =     [6, 8, 9, 11, 1, 2, 4, 5]
GMin =      [7, 9, 10, 0, 2, 3, 5, 6]
GSMin =     [8, 10, 11, 1, 3, 4, 6, 7]
AMin =      [9, 11, 0, 2, 4, 5, 7, 8]
ASMin =     [10, 0, 1, 3, 5, 6, 8, 9]
BMin =      [11, 1, 2, 4, 6, 7, 9, 10]

#define all keys in one array
AllKeys = [CMaj, CSMaj, DMaj, DSMaj, EMaj, FMaj, FSMaj, GMaj, GSMaj, AMaj, ASMaj, BMaj,
           CMin, CSMin, DMin, DSMin, EMin, FMin, FSMin, GMin, GSMin, AMin, ASMin, BMin]

KeyNames = ["C Maj", "CS Maj", "D Maj", "DS Maj", "E Maj", "F Maj", "FS Maj", "G Maj", "GS Maj", "A Maj", "AS Maj", "B Maj",
            "C Min", "CS Min", "D Min", "DS Min", "E Min", "F Min", "FS Min", "G Min", "GS Min", "A Min", "AS Min", "B Min"]


def findSimular(keyArr, testArr):
    simularNotes = []

    #increments through each note in the inputed array
    for note in testArr:

        #increments through each octave
        for i in range(0, 11):

            #increments through each note in the test array
            for compareNote in keyArr:
                
                if note == compareNote + (12 * i):
                    simularNotes.append(note)
    
    return simularNotes



def findKey(testArr):
    percentageSimular = []
    simularNotes = []


    #increments through each key to test
    for key in AllKeys:
        tempArr = findSimular(key, testArr)

        percentageSimular.append( (len(tempArr) / len(testArr)) * 100)
        simularNotes.append(tempArr)

    return percentageSimular, simularNotes


def printResults(testArr):
    percentageSimular, simularNotes = findKey(testArr)

    for perc, notes, names in zip(percentageSimular, simularNotes, KeyNames):
        print("Key name: ", end="")
        print(names, end="        ")
        print("Percentage Simular: ", end="")
        print(perc, end="")
        
        print(notes)

    sortedPerc = list(percentageSimular)
    sortedPerc.sort(reverse=True)

    print("Highest result: ", end="")

    print(KeyNames[percentageSimular.index(sortedPerc[0])])
    #print(sortedPerc[0])

#printResults([0, 2, 4, 5, 12, 23, 65, 73])


