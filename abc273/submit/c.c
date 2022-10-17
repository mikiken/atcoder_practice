/******************************
        Not Working
*******************************/

#include <stdbool.h>
#include <stdio.h>

bool is_include_num(int *x, int n, int num) {
  for (int i = 1; i <= n; i++) {
    if (x[i] == num)
      return true;
  }
  return false;
}

int main(int argc, char const *argv[]) {
  int n;
  int a[22] = {0};

  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &a[i]);
  }

  for (int k = 0; k < n; k++) {
    int include_num[22] = {0};
    int kind_num = 0;
    int arr_count = 0;
    int kind = 0;
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if (a[j] > a[i] && !is_include_num(include_num, n, a[j])) {
          include_num[arr_count++] = a[j];
          kind_num++;
        }
      }
      if (kind_num == k)
        kind++;
    }
    printf("%d\n", kind);
  }

  return 0;
}
