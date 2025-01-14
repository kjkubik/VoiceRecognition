
def lengthOfLongestSubstring(s: str) -> int:
    # Dictionary to store the last index of each character
    char_map = {}
    left = 0  # Left pointer of the sliding window
    max_length = 0

    # Traverse through the string with the right pointer
    for right in range(len(s)):
        # If the character is already in the window, move the left pointer
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1  # Move the left pointer to the right of the last occurrence
            print("left:", left)

        # Update the last index of the character
        char_map[s[right]] = right
        print(right)

        # Calculate the length of the current valid substring
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abbabcdadbkewekjgerjksgvlakbskjdskjdkjsdkjdjkj"

print(lengthOfLongestSubstring(s))