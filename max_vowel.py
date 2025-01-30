class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current_vowel_count = sum(char in vowels for char in s[:k])
        max_vowel_count = current_vowel_count

        for i in range(k, len(s)):
            current_vowel_count += s[i] in vowels
            current_vowel_count -= s[i - k] in vowels

            max_vowel_count = max(current_vowel_count, max_vowel_count)
        return max_vowel_count
