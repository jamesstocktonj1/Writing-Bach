#chord manipulation
#James Stockton
#27/03/19


#major keys
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



def getChord(scale, chord, seventh):
    #scale is the array of the notes in the scale
    #chord is the chord number I, II, ..., VII
    #seventh is a boolean on whether the chord has a seventh or not

    finChord = []
    
    chordLeng = 0
    if seventh:
        chordLeng = 4
    else:
        chordLeng = 3

    currNote = chord - 1
    for note in range(chordLeng):

        #print((chord - 1) + (2 * note))

        if ((chord - 1) + (2 * note)) > 6:
            finChord.append(scale[((chord - 1) + (2 * note)) - 6])
        else:
            finChord.append(scale[(chord - 1) + (2 * note)])
        """
        if len(finChord) == 0:
            finChord.append(scale[currNote])
        else:
            currNote += 2
            while currNote > 11:
                currNote -= 12
                
            finChord.append(scale[currNote])
        """
    return finChord
