def solution(m, musicinfos):
    answer = ''
    
    musicMap = {}
    playTimes = {}
    startTimes = {}
    
    m = m.replace("C#", "c").replace("D#", 'd').replace("F#", 'f').replace("G#",'g').replace('A#', 'a')
    
    def convertToMin(s):
        h,m = list(map(int, s.split(":")))
        return h*60 + m
    
    for el in musicinfos:
        s, e, name, note = el.split(",")
        s_m = convertToMin(s)
        e_m = convertToMin(e)
        play_time = e_m - s_m
        playTimes[name] = play_time
        startTimes[name] = s_m
        note = note.replace("C#", "c").replace("D#", 'd').replace("F#", 'f').replace("G#",'g').replace('A#', 'a')
        full_note = note*(play_time//len(note)) + note[:play_time%len(note)]
        musicMap[name] = full_note
        
    result = []
    for key, val in musicMap.items():
        if m in val:
            result.append(key)

    if len(result) == 0: return '(None)'
    result = sorted(result, key = lambda x: (-playTimes[x], startTimes[x]))
    
    return result[0]