class Solution:
    """
    store elements of J in a set
    iterate through S
    for each elem in S
        if elem is in set J
            then increment result
    return reselt
    
    runtime of this is linear O(n) where n = length of s
    space complexity for this is size of J
    """
    def numJewelsInStones(self, J: str, S: str):
        j = set(list(J))
        numJewels = 0
        for s in S:
            numJewels += 1 if s in j else 0
        return numJewels