#filling in chords to a set melody
#James Stockton
#03/04/19

from chord import *
from keyfinder import *

mel = [0, 2, 4, 6, 3, 7, 12, 9]
testChords = [0, 0, 0, 0, 0, 0, 0, 0]

chordPreference = [1, 4, 5, 6, 3, 2, 7]



"""
    endChord
    args - melody - array of the notes in the melody (length more than 0)
         - scale - the array of the decided key scale
    return - 

"""
def endChord(melody, scale):
    #gets the final note and makes it universal
    endNote = noteUniversal(melody[len(melody) - 1])
    #print("End note " + str(endNote))

    cadenceChords = [1, 5, 6, 4]

    #itterates through the prefered chords
    for chord in cadenceChords:
        #print("Chord " + str(chord))
        
        #iterates through the notes in that chord
        for note in getChord(scale, chord, False):
            
            #print("Chord notes " + str(getChord(scale, chord, False)))

            if note == endNote:
                return chord

    return "None"


    """
    if statements not working ??
    if bool(endNote in list(getChord(scale, 1, False))):
        return 1                                    #perfect cadence
    elif endNote in list(getChord(scale, 5, False)):
        return 5                                    #imperfect cadence
    elif endNote in list(getChord(scale, 4, False)):
        return 4                                    #imperfect / plagal cadance
    elif endNote in list(getChord(scale, 6, False)):
        return 6                                    #interrupted cadance
    else:
        return None                                 #returns none if no finishing chord found
    """






"""
    getCadence
    args - melody - array of the notes in the melody (length more than 0)
         - chords - array of the chord numbers( I, II, ... VII) same length as melody
         - scale - the array of the decided key scale
"""
def getCadence(melody, chords, scale):
    cadenceError = False

    #finds the final chords and sets the chord array to that value
    finChord = endChord(melody, scale)
    chords[len(melody)-1] = finChord

    #gets the penultimate note from the melody array
    penultimateNote = noteUniversal(melody[len(melody) - 2])

    #handles perfect cadences
    if finChord == 1:
        if penultimateNote in getChord(scale, 5, False):
            chords[len(melody)-2] = 5
        elif penultimateNote in getChord(scale, 4, False):
            chords[len(melody)-2] = 4
        elif penultimateNote in getChord(scale, 1, False):
            if noteUniversal(melody[len(melody) - 3]) in getChord(scale, 5, False):
                chords[len(melody)-2] = 1
                chords[len(melody)-3] = 5
            elif noteUniversal(melody[len(melody) - 3]) in getChord(scale, 4, False):
                chords[len(melody)-2] = 1
                chords[len(melody)-3] = 4
            else:
                cadenceError = True
        else:
            cadenceError = True

    #handles imperfect cadence
    elif finChord == 5:
        if penultimateNote in getChord(scale, 1, False):
            chords[len(melody)-2] = 1
        elif penultimateNot in getChord(scale, 4, False):
            chords[len(melody)-2] = 4
        else:
            cadenceError = True

    elif finChord == 4:
        if penultimateNote in getChord(scale, 1, False):
            chords[len(melody)-2] = 1
        elif penultimateNote in getChord(scale, 5, False):
            chords[len(melody)-2] = 5
        else:
            cadenceError = True

    elif finChord == 6:
        if penultimateNote in getChord(scale, 1, False):
            chords[len(melody)-2] = 1
        else:
            cadenceError = True

    else:
        #cadence error if no last chord is found
        smalestDif = [0, -1, 0]         #note, difference, chord num

        
        for i in range(0, 10):

            pass

    #if there is a cadence error
    if cadenceError:
        pass
    

    


def basicFill(melody, chords, scale):
    pass
