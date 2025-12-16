def lcs(s1: str, s2: str) -> str:
    dp = [[""] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = ""

    for i in range(len(s1) + 1):
        dp[i][0] = ""
    for j in range(len(s2) + 1):
        dp[0][j] = ""

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    return dp[-1][-1]
