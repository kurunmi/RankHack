#!/usr/bin/python3.6

def repchar(s):
        currstr = ""
        laststr = ""
        collector = {}
        for index, value in enumerate(s):
            if value not in collector:
                currstr += value
                collector[value] = index
            elif value in collector:
                if len(currstr) > len(laststr):
                    laststr = currstr
                currstr = currstr[collector[value]+1:]
                collector = {}
                for cur_index, cur_value in enumerate(currstr):
                    collector[cur_value] = cur_index
                currstr += value
                collector[value] =
                print(currstr, laststr)
        return max(len(laststr), len(currstr))


if __name__ == '__main__':
    s = "abcabcbb"
    t = "bbbbb"
    u = "pwwkew"
    print(repchar(u))