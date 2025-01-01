
class Solution:
    def findDuplicates(self, arr):
        res=set()
        dup=[]
        if not arr:
            return None
        for i in range(len(arr)):
            if arr[i] not in res:
                res.add(arr[i])
            else:
                dup.append(arr[i])
        return dup


        



#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates
    # Sort the result in ascending order
    s.sort()
    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends