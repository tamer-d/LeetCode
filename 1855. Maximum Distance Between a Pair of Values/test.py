from solution import Solution

def read_array(prompt):
    s = input(prompt).strip()
    if not s:
        return []
    if ',' in s:
        parts = [p.strip() for p in s.split(',') if p.strip() != ""]
    else:
        parts = [p for p in s.split() if p != ""]
    try:
        return [int(x) for x in parts]
    except ValueError:
        print("Entrée invalide : veuillez entrer des entiers séparés par des espaces ou des virgules.")
        return read_array(prompt)

if __name__ == "__main__":
    print("Entrez nums1 (tableau, éléments séparés par des espaces ou des virgules).")
    nums1 = read_array("nums1 : ")

    print("\nEntrez nums2 (tableau, éléments séparés par des espaces ou des virgules).")
    nums2 = read_array("nums2 : ")

    sol = Solution()
    res = sol.maxDistance(nums1, nums2)
    print("\nRésultat (distance maximale) :", res)
