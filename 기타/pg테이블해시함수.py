import operator

def solution(data, col, row_begin, row_end):
    answer = 0
    
    # 정렬
    sorted_data = sorted(data, key = lambda x: (x[col-1], -x[0]))
    
    xor = -1
    for i in range(row_begin-1, row_end):
        row = sorted_data[i]
        sum = 0
        for k in row:
            sum += k%(i+1)
        if xor == -1: xor = sum
        else: xor = operator.xor(xor, sum) 
   
    return xor