class Solution:
    def subarrayXor(self, arr, k):
        prefix_xors = {0 : 1}
        c_xor, cnt = 0, 0
        
        for ele in arr:
            c_xor ^= ele
            if c_xor^k in prefix_xors:
                cnt += prefix_xors[c_xor ^ k]

            prefix_xors[c_xor] = prefix_xors.get(c_xor,0) + 1
        return cnt

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends
