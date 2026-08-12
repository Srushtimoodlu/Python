class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        ans = []

        k -= 1  # Convert k to 0-based index

        for i in range(n, 0, -1):
            fact = 1
            for j in range(1, i):
                fact *= j

            index = k // fact
            ans.append(str(nums[index]))
            nums.pop(index)

            k %= fact

        return ''.join(ans)
        