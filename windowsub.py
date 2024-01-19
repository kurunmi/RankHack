#!/usr/bin/python3
import copy


def windowsub(s, t):
    final_sub = ""
    t_dict = {}
    s_dict = {}
    t_len = len(t)
    if t > s:
        return final_sub
    for char in t:
        if char not  in t_dict:
            t_dict[char] = 1 + t_dict.get(char, 0)
    needed = len(t_dict)
    for index, value in enumerate(s):
        if value in t_dict:
            tmp_dict = copy.deepcopy(t_dict)
            sub_str = s[index:]
            current_sub = ""
            if t_len <= len(sub_str):
                for char in sub_str:
                    current_sub += char
                    if char in tmp_dict:
                        tmp_dict[char] -= 1
                        if tmp_dict[char] < 1:
                            del tmp_dict[char]
                        if len(tmp_dict) < 1:
                            if final_sub:
                                if len(current_sub) < len(final_sub):
                                    final_sub = current_sub
                            else:
                                final_sub = current_sub
                            current_sub = ""
    return final_sub

if __name__ == '__main__':
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(windowsub(s1, t1))
