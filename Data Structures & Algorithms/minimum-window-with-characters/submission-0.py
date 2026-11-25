class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        have = 0
        need_count = len(need)

        left = 0
        min_length = float("inf")
        result = ""

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            # Window contains all required characters
            while have == need_count:
                current_length = right - left + 1

                if current_length < min_length:
                    min_length = current_length
                    result = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result
        