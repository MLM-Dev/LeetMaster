class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0
        for right in range(len(s)):
            current_char = s[right]
            if current_char in char_index and char_index[current_char] >= left:
                left = char_index[current_char] + 1
            char_index[current_char] = right
            current_window = right - left + 1
            if current_window > max_length:
                max_length = current_window
        return max_length