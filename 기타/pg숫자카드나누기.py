import math

def solution(arrayA, arrayB):
    def getGCD(arr):
        gcd = arr[0]
        for i in range(1, len(arr)):
            gcd = math.gcd(gcd, arr[i])
        return gcd
    
    gcd_a = getGCD(arrayA)
    gcd_b = getGCD(arrayB)

    def getDiv(number):
        result = []
        for i in range(1, math.floor(math.sqrt(number))):
            if number%i == 0:
                result.append(int(i))
                result.append(int(number/i))
        return result
    
    def getA(gcd, list):
        divs = getDiv(gcd)
        divs.sort(reverse=True)
        for num in divs:
            flag = 1
            for i in list:
                if i%num == 0: flag = 0;
            if flag == 1: return num
        return 0
    
    return max(getA(gcd_b, arrayA), getA(gcd_a, arrayB))