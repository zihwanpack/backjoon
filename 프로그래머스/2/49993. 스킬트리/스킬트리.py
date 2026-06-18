def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        filterd_skill = ''
        for candidate_skill in skill_tree:
            if candidate_skill in skill:
                filterd_skill += candidate_skill
                
        if skill.startswith(filterd_skill):
            answer += 1
            
    return answer