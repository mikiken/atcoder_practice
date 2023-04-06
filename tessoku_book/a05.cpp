#include <iostream>
using namespace std;

int main() {
  int N, K;
  cin >> N >> K;

  int count = 0;
  for (int r = 1; r <= N; ++r) {
    for (int b = 1; b <= N; ++b) {
      int w = K - r - b;
      if (1 <= w && w <= N)
        ++count;
    }
  }
  cout << count << endl;
}