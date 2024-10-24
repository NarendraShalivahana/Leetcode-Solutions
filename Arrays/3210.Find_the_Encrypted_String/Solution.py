class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        nums=[i for i in s];n=len(s)
        s=nums.copy()
        for i in range(n):
            s[i]=nums[(i+k)%n]
        return "".join(s)
