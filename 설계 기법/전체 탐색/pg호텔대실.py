def solution(book_time):
    def convert_min(s):
        h, m = list(map(int, s.split(":")))
        return h*60 + m
    def convert_book_time_min(el):
        return list(map(convert_min, el))
    
    cnt = [0]*24*60
    book_time_min = list(map(convert_book_time_min, book_time))
    print(book_time_min)
    
    for i in range(len(cnt)):
        for k in book_time_min:
            if k[0] <= i and k[1] + 10 > i: cnt[i] += 1

    return max(cnt)