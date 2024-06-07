def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    longest = 0
    for index in range(len(s)):
        print(index)
        if s[index] not in seen:
            seen.add(s[index])
            longest = max(longest, index + 1 - left)
        else:
            while s[index] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[index])
    return longest

if __name__ == '__main__':
    s="abcabcbb"
    s1 = "pwwkew"
    s2 = "abcbcadaefgh"
    s3 = "dvdh"
    print(lengthOfLongestSubstring(s))