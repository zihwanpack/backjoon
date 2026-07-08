def solution(n, costs):
    answer = 0
    bridge_count = 0
    rosts = [i for i in range(n)]
    
    
    costs.sort(key=lambda x : x[2])
    
    def get_root_node(x):
        if x == rosts[x]:
            return x
        rosts[x] = get_root_node(rosts[x])
        return  rosts[x]
    
    def union(a, b):
        a = get_root_node(a)
        b = get_root_node(b)
        if a < b:
            rosts[b] = a
        else:
            rosts[a] = b
    
    for a, b, weight in costs:
        if get_root_node(a) != get_root_node(b):
            union(a, b)
            answer += weight
            bridge_count += 1
        
        if bridge_count == n - 1:
            break
        
    return answer