from collections import defaultdict

class Solution:

    def anagrams(self, arr):
        
        anagram_groups = defaultdict(list)
        for word in arr:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)

        result = [anagram_groups[key] for key in anagram_groups]
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends