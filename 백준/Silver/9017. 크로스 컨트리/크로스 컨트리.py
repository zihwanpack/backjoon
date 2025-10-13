import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  data = list(map(int, input().split()))

  # 딕셔너리로 각 팀의 멤버 수 카운트
  count_teams = {}
  for player in data:
    if player in count_teams:
      count_teams[player] += 1 
    else:
      count_teams[player] = 1
  
  verified_teams = []
  for team, count in count_teams.items():
    if count == 6:
      verified_teams.append(team)

  # 각 팀 점수 계산할 딕셔너리 초기화
  teams_scores = {}
  for team in verified_teams:
    teams_scores[team] = []
  
  current_score = 1
  for team in data:
    if team in verified_teams:
      teams_scores[team].append(current_score)
      current_score += 1
  # 최종 등수 계산 후 등수 비교
  results = []
  
  for team, score in teams_scores.items():
    sum_of_score = sum(score[:4])
    fifth_score = score[4]
    results.append([sum_of_score, fifth_score, team])

  results.sort()
  winner = results[0][2]
  print(winner)