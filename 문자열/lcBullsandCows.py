class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_cnt = [0]*10
        guess_cnt = [0]*10

        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else: 
                secret_cnt[int(secret[i])] += 1
                guess_cnt[int(guess[i])] += 1

        cows = 0
        for i in range(10):
            if secret_cnt[i] <= guess_cnt[i]: cows += secret_cnt[i]
            else: cows += guess_cnt[i]

        return str(bulls)+"A"+str(cows)+"B"