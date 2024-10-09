class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_freq = Counter(magazine)
        ransomNote_freq = Counter(ransomNote)
        
        for each in ransomNote:
            if ransomNote_freq[each] > magazine_freq[each]:
                return False
        return True