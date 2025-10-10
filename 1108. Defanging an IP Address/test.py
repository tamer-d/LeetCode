class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

if __name__ == "__main__":
    address = input("Entrez une adresse IP : ")
    sol = Solution()
    print("Adresse IP defangée :", sol.defangIPaddr(address))