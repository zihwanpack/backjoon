import sys
input = sys.stdin.readline

N, M = map(int, input().split())

verified_words = {}

def sort_words(words):
  word_list = list(words.items())
  """ 
  key=lambda x: (-x[1], -len(x[0]), x[0]) 부분은 다음과 같은 의미입니다.
  -x[1]: 첫 번째 기준. 횟수(x[1])를 기준으로 내림차순(-) 정렬합니다.
  -len(x[0]): 두 번째 기준. 단어(x[0])의 길이를 기준으로 내림차순(-) 정렬합니다.
  x[0]: 세 번째 기준. 단어(x[0]) 자체를 기준으로 오름차순(사전 순) 정렬합니다.
  Python은 key에 튜플 ()을 넘겨주면, `앞의 기준으로 정렬을 시도하고 값이 같을 경우 자동으로 다음 기준으로 넘어갑니다. 이 기능을 활용하면 복합적인 정렬 조건을 간결하게 처리할 수 있습니다. 
  """
  sorted_list = sorted(word_list, key=lambda x: (-x[1], -len(x[0]), x[0]))
  return sorted_list

for _ in range(N + 1):
  word = input().rstrip()
  if len(word) >= M and word not in verified_words:
    verified_words[word] = 1
  elif len(word) >= M:
    verified_words[word] += 1  

sorted_list = sort_words(verified_words)

for word,count in sorted_list:
  print(word)