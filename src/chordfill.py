#filling in chords to a set melody
#James Stockton
#03/04/19

from chord import *
from keyfinder import *







"""
    endChord
    args - melody - array of the notes in the melody (length more than 0)
         - scale - the array of the decided key scale
    return - 

"""
def endChord(melody, scale):
    #gets the final note and makes it universal
    endNote = noteUniversal(melody[len(melody) - 1])

    if endNote in getChord(scale, 1, False):
        return 1                                    #perfect cadence
    elif endNote in getChord(scale, 5, False):
        return 5                                    #imperfect cadence
    elif endNote in getChord(scale, 4, False):
        return 4                                    #imperfect / plagal cadance
    elif endNote in getChord(scale, 6, False):
        return 6                                    #interrupted cadance
    else:
        return None                                 #returns none if no finishing chord found
    

    


def basicFill(melody, chords, scale):
    
