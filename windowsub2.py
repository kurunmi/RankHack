#!/usr/bin/python3
import copy


def windowsub(s, t):
    if len(s) < len(t):
        return ""
    sub_str = ""
    all_subs = []
    t_dict = {}
    s_dict = {}
    outer_index = 0
    for char in t:
        t_dict[char] = 1 + t_dict.get(char, 0)
    required_keys = len(t_dict)
    needed_keys = 0
    for index, value in enumerate(s):
        status = False
        if value in t_dict:
            s_dict[value] = 1 + s_dict.get(value, 0)
            if s_dict[value] == t_dict[value]:
                needed_keys += 1
        if needed_keys == required_keys:
            status = True
        while needed_keys == required_keys:
            if s[outer_index] in s_dict:
                s_dict[s[outer_index]] -= 1
                if s_dict[s[outer_index]] < t_dict[s[outer_index]]:
                    needed_keys -= 1
            outer_index += 1
        if needed_keys != required_keys and status:
            if not sub_str:
                sub_str = [outer_index - 1,index + 1]
            if sub_str[1] - sub_str[0] > (index +1) - (outer_index -1):
                sub_str = [outer_index - 1,index + 1]
    if sub_str:
        return s[sub_str[0]:sub_str[1]]
    return sub_str


if __name__ == '__main__':
    s1 = "ABRACADABRA"
    s2 = "ADOBECODEBANC"
    s3 = "cabwefgewcwaefgcf"
    t1 = "ABC"
    t2 = "cae"
    print(windowsub(s3, t2))