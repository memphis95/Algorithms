def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

    return True
"""
    Complexity Analysis:
        Time Complexity  : O(n) - perform approximately n iterations using
                                  two pointer technique
        Space Complexity : O(1) - using constant number of variables

"""

"""
    Test Cases:
        1. an empty string                           - ''
        2. a single-character string                 - 'a'
        3. a palindrome with two characters          - 'aa'
        4. a non-polindrome with two characters.     - 'ab'
        5. a string with no alphanumeric characters  - '!,(?)'
        6. a palindrome with punctuation and numbers - '12.02.2021'
        7. a non-palindrome with punctuation and numbers - '21.02.2021'
        8. a non-palindrome with punctuation   - 'hello, world!'


"""