# PossiblyAxolotl
# Other math
# Math functions I thought could be useful for future projects so I'm saving them here
# -=-=-=-=-=-=-=-=-=-=-=-=-
# Started Nov 6, 2023
# Last updated Nov 7, 2023 

def clamp(value, minimum, maximum):
    '''keeps 'value' between the min and max'''
    return max(min(value, maximum), minimum)

def lerp(from_value, to_value, by_value):
    '''linearly interpolates from 'from_value' to 'to_value' by 'by_value' which should be a value from 0 to 1'''
    return (to_value - from_value) * by_value

def between(value, minimum, maximum):
    '''quick function to check if 'value' is between the minimum and maximum'''
    return value > minimum and value < maximum

def between_circle_doorway(value, minimum, maximum, opening):
    '''like between but super specific to the circle doorways'''
    if value > opening and minimum + maximum < 0: # extra code needed to account for angles that go below 0 degrees
        value -= 359

    return between(value, minimum, maximum)