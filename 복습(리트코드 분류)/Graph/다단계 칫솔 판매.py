import math

def solution(enroll, referral, seller, amount):

    refDict = {}
    for i in range(len(enroll)):
        refDict[enroll[i]] = referral[i]
    
    resultDict = {}
    def distribute(amt, node):
        give = amt//10
        if node not in resultDict: resultDict[node] = 0 # 초기화
        resultDict[node] += amt - give
        if give == 0: return
        if node == "-": return
        distribute(give, refDict[node])
    
    for i in range(len(amount)):
        distribute(amount[i]*100, seller[i])
        
    result = [0]*len(enroll)
    for i in range(len(enroll)):
        result[i] = resultDict[enroll[i]] if enroll[i] in resultDict else 0
    
    return result