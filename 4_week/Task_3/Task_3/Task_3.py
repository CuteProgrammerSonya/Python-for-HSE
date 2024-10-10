# 204. Count Primes
# https://leetcode.com/problems/count-primes/description/?envType=problem-list-v2&envId=array


def countPrimes(n):
    sieve = [1 for i in range(0, n)]
    i = 2
    if n == 0 or n == 1:
        return 0
    count = n - 2
    while i**2 < n:
        if sieve[i] == 1:
            for j in range(i**2, n, i):
                if sieve[j] == 1:
                    count -= 1
                sieve[j] = 0
        i += 1
    return count


n = int(input())
print(countPrimes(n))

""" My solution in LeetCode:
class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [1 for i in range(0, n)]
        i = 2
        if n == 0 or n == 1:
            return 0
        count = n - 2
        while i ** 2 < n:
            if sieve[i] == 1:
                for j in range(i**2, n, i):
                    if sieve[j] == 1:
                        count -= 1
                    sieve[j] = 0
            i += 1
        return count
"""
