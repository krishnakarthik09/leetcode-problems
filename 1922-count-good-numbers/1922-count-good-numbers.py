
class Solution:
    def power(self, n, base, modulo):
        ans = 1

        while n > 0:
            if n % 2 == 1:
                ans = (ans * base) % modulo

            base = (base * base) % modulo
            n //= 2

        return ans

    def countGoodNumbers(self, n: int) -> int:
        modulo = (10**9) + 7

        even_indices = self.power((n + 1) // 2, 5, modulo)
        odd_indices = self.power(n // 2, 4, modulo)

        return (even_indices * odd_indices) % modulo
