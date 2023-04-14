class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = dict()
        def can_win(choices, remainder):
            if choices[-1] >= remainder:
                return True

            seen_key = tuple(choices)
            if seen_key in seen:
                return seen[seen_key]

            for index in range(len(choices)):
                if not can_win(choices[:index] + choices[index + 1:], remainder - choices[index]):
                    seen[seen_key] = True
                    return True

            seen[seen_key] = False
            return False

        summed_choices = (maxChoosableInteger + 1) * maxChoosableInteger / 2

        if summed_choices < desiredTotal:
            return False

        if summed_choices == desiredTotal: return maxChoosableInteger % 2

        choices = list(range(1, maxChoosableInteger + 1))
        return can_win(choices, desiredTotal)