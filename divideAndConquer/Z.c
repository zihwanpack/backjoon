#include <stdio.h>
#include <math.h>

int check (int N, int r, int c);

int main (void) {
  int N, r, c;
  scanf("%d %d %d", &N, &r, &c);
  int result = check(N, r, c);
  printf("%d", result);
  return 0;
}

int check (int N, int r, int c) {
  if (N < 1) return 0;
  
  int mid = (int)pow(2, N - 1);

  if (r < mid && c < mid) {
    return check(N - 1, r, c);
  } 
  else if (r < mid && c >= mid) {
    return mid * mid + check(N - 1, r, c - mid);
  }
  else if (r >= mid && c < mid) {
    return mid * mid * 2 + check(N - 1, r - mid, c);
  }
  else {
    return mid * mid * 3 + check(N - 1, r - mid, c - mid);
  }
}

