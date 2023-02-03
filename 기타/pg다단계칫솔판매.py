# 초기에 seller의 amount 전부 합한 후 dfs 했으나,
# 15 + 15 = 30 배분 시 3, 각각 할 시 1 + 1 = 2 => 여기서 틀림
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