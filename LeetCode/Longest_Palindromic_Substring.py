import sys

def longest_palindrome(s: str) -> str:
    if not s or len(s) < 1:
        return ""

    def expand_around_center(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Returns the indices bounding the valid palindrome
        return left + 1, right - 1

    start, end = 0, 0

    for i in range(len(s)):
        # Odd length palindromes (e.g., "aba")
        l1, r1 = expand_around_center(i, i)
        # Even length palindromes (e.g., "abba")
        l2, r2 = expand_around_center(i, i + 1)

        # Update the longest bounds found
        if (r1 - l1) > (end - start):
            start, end = l1, r1
        if (r2 - l2) > (end - start):
            start, end = l2, r2

    return s[start:end + 1]


# Standard Input / Output handling
if __name__ == "__main__":
    # Example input execution
    input_str = input("Enter string: ").strip()
    result = longest_palindrome(input_str)
    print(f"Longest Palindromic Substring: {result}")