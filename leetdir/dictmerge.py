def merge(dicts):
    dict1, dict2 = dicts
    outdict = {}
    conflict = {}
    for key in dict1:
        if key in dict2:
            conflict[key] = [dict1[key], dict2[key]]
        else:
            outdict[key] = dict1[key]
    for key in dict2:
        if key in dict1 and key not in conflict:
            conflict[key] = [dict1[key], dict2[key]]
        else:
            outdict[key] = dict2[key]
    return outdict
