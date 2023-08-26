def smith_waterman_modified(s1, s2, gap_penalty=-1, mismatch_penalty=-1):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    max_score = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            match_score = dp[i-1][j-1] + (1 if s1[i-1] == s2[j-1] else mismatch_penalty)
            dp[i][j] = max(
                dp[i-1][j] + gap_penalty,
                dp[i][j-1] + gap_penalty,
                match_score,
                0
            )
            max_score = max(max_score, dp[i][j])

    return max_score

s1 = "pattern"
s2 = "longtextwithpaxterninside"

result = smith_waterman_modified(s1, s2)
print("Highest Score:", result)

