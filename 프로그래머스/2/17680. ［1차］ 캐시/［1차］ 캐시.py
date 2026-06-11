from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    execution_time = 0
    cache_memory = deque()
    
    for city in cities:
        ## 문자열 소문자 전환
        city_lower = city.lower()
        ## cache hit 시
        if city_lower in cache_memory:
            execution_time += 1
            cache_memory.remove(city_lower)
            cache_memory.append(city_lower)
        ## cache miss 시
        else:
            execution_time += 5
            if len(cache_memory) >= cacheSize:
                cache_memory.popleft()
            cache_memory.append(city_lower)
            
        
    return execution_time