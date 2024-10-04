#include <stdio.h>
#define MAX 2187
#define TRUE 1
#define FALSE 0

int paper[MAX][MAX];
int answer[3];

void splitPaper (int x, int y, int N);
int checkPaper (int x, int y, int N);

int main (void) {
  int N;
  scanf("%d", &N);

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      scanf("%d", &paper[i][j]);
    }
  }
  splitPaper(0, 0, N);

  for (int k = 0; k < 3; k++) {
    printf("%d\n", answer[k]);
  }
  return 0;
}

int checkPaper (int x, int y, int N) {
  int initValue = paper[x][y];
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (paper[x + i][y + j] != initValue) return FALSE;
    }
  }
  return TRUE;
}

void splitPaper(int x, int y, int N) {
  if (checkPaper(x, y, N)) {
    answer[paper[x][y] + 1]++;
    return; 
  }
  // split 로직
  else {
    for (int i = 0; i < 3; i++) {
          for (int j = 0; j < 3; j++) {
            splitPaper(x + i * N / 3, y + j * N / 3, N / 3);
          }
        }
  } 
}

