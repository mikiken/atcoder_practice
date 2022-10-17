#include <stdio.h>

int recursive(int n) {
  if (n == 0)
    return 1;
  else
    return recursive(n - 1) * n;
}

int main(int argc, char const *argv[]) {
  int n;
  scanf("%d", &n);
  printf("%d", recursive(n));
  return 0;
}
