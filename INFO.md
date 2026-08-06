Input: logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act car"]
Output: ["a8 act car", "g1 act car", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]

Explanation:
- "a8 act car" comes before "g1 act car" because their contents are identical ("act car"), so we break the tie using their identifiers ("a8" < "g1").