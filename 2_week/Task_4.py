# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=string

def groupAnagrams(strs):
    key_table = {}
    for i in range(0, len(strs)):
            index = "".join(sorted(strs[i]))
            if index not in key_table:
                arr = []
                key_table[index] = arr
            key_table[index].append(strs[i])
    table = []
    for i in key_table.values():
        table.append(i) 
    return table

strs = []
count = int(input()) # using for debug
for i in range(0, count):
    string = input()
    strs.append(string)
print(groupAnagrams(strs))

""" Hash table solution
def groupAnagrams(strs):
    hash_table = [[] for i in range(0, len(strs))]
    for i in range(0, len(strs)):
        hash_value = 0
        for j in range(0, len(strs[i])):
            hash_value += ord(strs[i][j])
        hash_value %= len(strs)
        if not hash_table[hash_value]:
            hash_table[hash_value].append(strs[i])
        else:
            if sorted(hash_table[hash_value][0]) == sorted(strs[i]):
                hash_table[hash_value].append(strs[i])
            else:
                clear_index = 0
                flag = 0
                addition = 0
                for m in range(0, len(hash_table)):
                    if (not hash_table[m] and flag == 0):
                        clear_index = m
                        flag = 1
                    if (hash_table[m]):
                        if (sorted(strs[i]) == sorted(hash_table[m][0])):
                            hash_table[m].append(strs[i])
                            addition = 1
                            break
                if addition == 0:
                    print(clear_index, " ")
                    hash_table[clear_index].append(strs[i])
    table = []
    for i in range(0, len(hash_table)):
        if hash_table[i]:
            table.append(hash_table[i])
    return table
"""
""" My solution in LeetCode
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_table = {}
        for i in range(0, len(strs)):
            index = "".join(sorted(strs[i]))
            if index not in key_table:
                arr = []
                key_table[index] = arr
            key_table[index].append(strs[i])
        table = []
        for i in key_table.values():
            table.append(i) 
        return table
"""
        