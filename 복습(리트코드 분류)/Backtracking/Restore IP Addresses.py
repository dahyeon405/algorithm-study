class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        results = []
        n = len(s)

        def dfs(idx, dotsCnt, prefix):
            if (dotsCnt == 3 and idx < n and int(s[idx:]) <= 255):
                if (s[idx] == '0' and n - idx > 1): return
                results.append(prefix + s[idx:])
                return

            for i in range(1, min(4, n-idx+1)):
                if (int(s[idx:idx+i]) > 255): break
                else: dfs(idx+i, dotsCnt + 1, prefix + s[idx:idx+i] + ".")
                if (s[idx] == '0'): break

            return

        dfs(0, 0, "")

        return results