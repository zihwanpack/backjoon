import sys
input = sys.stdin.readline

vowels = 'aeiou'

def is_vowel (char):
  return char in vowels 

def acceptable (password):
  if not any(is_vowel(ch) for ch in password):
    return False
  for i in range(len(password) - 2):
    if is_vowel(password[i]) and is_vowel(password[i + 1]) and is_vowel(password[i + 2]):
      return False
    if is_vowel(password[i]) == False and is_vowel(password[i + 1]) == False and is_vowel(password[i + 2]) == False:
      return False
  for i in range(len(password) - 1):
    if password[i] == password[i + 1]:
      if password[i] != 'e' and password[i] != 'o':
        return False
  return True

while True:
  password = input().strip()

  if password == 'end':
    break

  if acceptable(password):
        print(f"<{password}> is acceptable.")
  else:
        print(f"<{password}> is not acceptable.")


