'''
Write a python function, check_anagram() which accepts two strings and returns True, if one string is an anagram of another string. 
Otherwise returns False.

The two strings are considered to be an anagram if they contain repeating characters but none of the characters repeat at the same position.
The length of the strings should be the same.
'''

#PF-Assgn-54
def check_anagram(data1,data2):
    #start writing your code here
    data1 = data1.lower()
    data2 = data2.lower()

    if len(data1) != len(data2):
        return False

    if sorted(data1) != sorted(data2):
        return False

    for i in range(len(data1)):
        if data1[i] == data2[i]:
            return False

    return True

print(check_anagram("About","table"))
