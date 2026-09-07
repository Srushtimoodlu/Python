class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * 26
        
        for ch in s:
            i = ord(ch) - ord('a')
            total = 1
            
            for x in dp:
                total = (total + x) % MOD
            
            dp[i] = total
        
        return (sum(dp) % MOD)
        