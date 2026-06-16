def make_sorted_groups(s):
    
    ## 양 끝 괄호를 떼고 '},{' 기준으로 쪼개서 문자열 그룹 만들기
    string_groups = s.lstrip('{{').rstrip('}}').split('},{')
    
    ## 각 문자열 그룹을 진짜 숫자 리스트로 변환
    total_groups = []
    for group in string_groups:
        numbers = [int(num_str) for num_str in group.split(',')]
        total_groups.append(numbers)
        
    ## 그룹 안에 든 숫자의 개수(길이)가 짧은 순서대로 정렬 후 반환.
    return sorted(total_groups, key=len)


def solution(s):
    answer = []
    
    # 정렬된 숫자 그룹들을 가져오기
    sorted_groups = make_sorted_groups(s)
    
    # 각 그룹을 하나씩 확인하면서 정답 리스트를 채웁니다.
    for group in sorted_groups:
        for num in group:
            if num not in answer:
                answer.append(num)
                
    return answer