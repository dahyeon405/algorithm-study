def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)):
        for k in range(i+1, len(phone_book)):
            if phone_book[k].startswith(phone_book[i]):
                return False
            else: break

    return True

# 다른 사람의 해시맵 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer