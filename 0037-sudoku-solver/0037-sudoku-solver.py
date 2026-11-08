class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    bit = 1 << (int(board[r][c]) - 1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def solve(n):
            # n = how many empty cells are left (in empty[0:n])
            if n == 0:
                return True

            # find the cell with the fewest choices
            best = -1
            best_mask = 0
            best_count = 10
            for i in range(n):
                r, c = empty[i]
                used = rows[r] | cols[c] | boxes[(r // 3) * 3 + c // 3]
                avail = ~used & 511
                cnt = bin(avail).count('1')
                if cnt < best_count:
                    best, best_mask, best_count = i, avail, cnt
                    if cnt == 0:
                        return False
                    if cnt == 1:
                        break

            # move chosen cell to the end of the active part
            empty[best], empty[n - 1] = empty[n - 1], empty[best]
            r, c = empty[n - 1]
            b = (r // 3) * 3 + c // 3

            mask = best_mask
            while mask:
                bit = mask & -mask      # take lowest digit
                mask ^= bit
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                board[r][c] = str(bit.bit_length())

                if solve(n - 1):
                    return True

                # undo
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit

            board[r][c] = '.'
            return False

        solve(len(empty))