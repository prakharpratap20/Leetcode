class Solution:
    def merge_alternately(self, word1, word2):
        i, j = 0, 0
        result = []

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        result.append(word1[i:])
        result.append(word2[j:])

        return "".join(result)


N1 = "abc"
W2 = "pqr"

ans = Solution()
