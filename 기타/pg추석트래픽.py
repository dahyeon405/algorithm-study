def convertToSec(time):
    [h, m, s] = list(map(float, time.split(":")))
    h = int(h*3600*1000)
    m = int(m*60*1000)
    s = int(s*1000)
    return h + m + s

def solution(lines):
    inputs = []
    
    for i in lines:
        [_, time, dur] = i.split(" ");
        t = convertToSec(time)
        start_t = t - int(float(dur[0:-1])*1000)+1
        inputs.append([start_t, t])
    
    sortedTime = sorted(inputs, key=lambda x: x[1])
    
    print(sortedTime)
    max = 0
    for i in range(len(sortedTime)):
        end = sortedTime[i][1]
        nextEnd = end + 999
        count = 1
        print(end, nextEnd)
        for k in range(i+1, len(sortedTime)):
            if sortedTime[k][1] >= end and sortedTime[k][0] <= nextEnd: count += 1
            elif sortedTime[k][1] == end or sortedTime[k][0] == 1: count += 1
        if count > max:
            max = count
    
    return max