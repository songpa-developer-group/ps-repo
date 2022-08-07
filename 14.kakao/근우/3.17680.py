def solution(cacheSize, cities):
    answer = 0
    i = 0              # 초기 캐시 인덱스
    cache = []
    if cacheSize == 0:                # 캐시 사이즈가 0이면,
        return len(cities)*5
    for c in cities:
        city = c.upper()              # city 이름 대문자 통일
        if city in cache:             # 캐시에 이미 있는 city의 경우
            cache.remove(city)        # 해당 city 캐시에서 위치 재조정
            cache.append(city)
            answer += 1
        else:                         # 캐시에 없는 city의 경우
            answer += 5
            if i < cacheSize:         # 아직 캐시에 빈 공간이 있다면
                cache.append(city)
                i += 1
            else:                     # 캐시에 빈 공간이 없다면
                cache.pop(0)          # 캐시 내부 city 하나 교체
                cache.append(city)

    return answer