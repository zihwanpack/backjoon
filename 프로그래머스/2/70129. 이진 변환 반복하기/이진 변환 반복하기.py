def solution(s):
    transfer_count = 0
    deleted_count = 0
    remove_char = '0'
    
    while s != "1":
        one_count = s.count('1')
        deleted_count += len(s) - one_count
        s = bin(one_count)[2:]
        transfer_count += 1
                
        
    
    
    return [transfer_count, deleted_count]