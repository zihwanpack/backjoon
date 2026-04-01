from collections import deque
def solution(word):
    dictionary = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    queue = deque([''])
    
    while queue:
        current_word = queue.popleft()
        if len(current_word) < 5:
            for vowel in vowels:
                next_word = current_word + vowel
                queue.append(next_word)
                dictionary.append(next_word)
                
    dictionary.sort()
    return dictionary.index(word) + 1