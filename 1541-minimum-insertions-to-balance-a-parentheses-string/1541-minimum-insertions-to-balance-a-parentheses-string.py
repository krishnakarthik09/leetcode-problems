class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        count = 0
        open_count = 0
        i = 0

        while i < n:
            if s[i] == '(':
                open_count += 1
            else:
                # Check for the required pair ))
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    count += 1

                # No opening bracket available
                if open_count > 0:
                    open_count -= 1
                else:
                    count += 1

            i += 1

        # Each unmatched '(' needs two ')'
        count += open_count * 2

        return count