#!/usr/bin/python3
import math

def get_all_minutes(timestr, attrib):
    hr, min = timestr.split(':')
    if attrib == 'hr':
        return (int(hr) * 60 + int(min))
    if attrib == 'min':
        return int(min)
    return timestr


def get_val(mins, mytotal, unit):
    maxrad = 2 * math.pi
    unitmap = {'radians':maxrad, 'degrees':360}
    outval = mins/mytotal * unitmap[unit]
    if unit == 'degrees':
        return int(outval)
    if unit == 'radians':
        return round(float(outval), 4)



def getangle(timest, unit):
    hour_total = 12 * 60
    minute_total = 60
    hour_mins = get_all_minutes(timest, 'hr')
    hour_val = get_val(hour_mins, hour_total, unit)
    mins = get_all_minutes(timest, 'min')
    minute_val = get_val(mins, minute_total, unit)
    diff = abs(hour_val - minute_val)
    return diff


if __name__ == '__main__':
    print(getangle('03:00', 'radians'))