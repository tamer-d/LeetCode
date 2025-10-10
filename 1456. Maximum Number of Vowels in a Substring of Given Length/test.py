class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        max_count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_count = max(max_count, count)

        return max_count

if __name__ == "__main__":
    s = input("Entrez la chaîne : ")
    k = int(input("Entrez la longueur k : "))
    sol = Solution()
    print("Maximum de voyelles dans une sous-chaîne de longueur", k, ":", sol.maxVowels(s, k))
