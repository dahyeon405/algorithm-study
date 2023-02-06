def convertToSec(time):
    [a, b, c] = list(map(int, time.split(":")))
    return a*60*60 + b*60 + c

def convertBack(num):
    h = num//3600
    m = (num%3600)//60
    s = num%60
    arr = [str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)]
    return ":".join(arr)
    
def solution(play_time, adv_time, logs):
    play_time_sec = convertToSec(play_time)
    adv_time_sec = convertToSec(adv_time)
    
    total_time = [0]*(play_time_sec+1)
    
    for i in logs:
        [s, e] = list(map(convertToSec, i.split("-")))
        total_time[s] += 1
        total_time[e] -= 1
        
    #total_time[i] = i ~ i+1 구간 개수
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i-1] + total_time[i]
        
    #total_time[i] = 0~i+1 누적 재생 시간
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i-1] + total_time[i]
    
    # 구간 총 재생 시간 구하기
    # total_time[b] - total_time[a]: a-1번째 누적
    
    # i는 구간 종료 시간
    max = 0
    answer = 0
    for i in range(adv_time_sec, play_time_sec + 1):
        if i == adv_time_sec:
            t = total_time[i]
            if t > max:
                max = t        
        t = total_time[i] - total_time[i - adv_time_sec]
        if t > max: 
            answer = i - adv_time_sec + 1
            max = t
    
    answer = convertBack(answer)
    return answer