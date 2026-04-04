class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        if rows == 0:
            return ""

        cols = len(encodedText) // rows
        result = ""

        # Parcourir chaque colonne de départ
        for start_col in range(cols):

            i = 0
            j = start_col

            # Parcours diagonal
            while i < rows and j < cols:
                index = i * cols + j
                result += encodedText[index]

                i += 1
                j += 1

        return result.rstrip()
