#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(int x) {
    long int reverted = 0;
    int original = x;
    while (x > 0) {
        reverted = reverted * 10 + x % 10;
        x /= 10;
    }
    return original == reverted;
}

int main() {
    int n = 12321;

    if (isPalindrome(n)) {
        printf("PALINDROMO\n", n);
    } else {
        printf("NO PALINDROMO\n", n);
    }

    return 0;
}