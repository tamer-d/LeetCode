class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        def days_from_0(date):
            year, month, day = map(int, date.split('-'))
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            days = 365 * year + year // 4 - year // 100 + year // 400

            for m in range(month - 1):
                days += days_in_month[m]

            # Si c’est une année bissextile et que le mois est après février
            if month > 2 and is_leap(year):
                days += 1

            days += day
            return days

        return abs(days_from_0(date1) - days_from_0(date2))

if __name__ == "__main__":
    date1 = input("Entrez la première date (YYYY-MM-DD): ")
    date2 = input("Entrez la deuxième date (YYYY-MM-DD): ")
    sol = Solution()
    print("Nombre de jours entre les deux dates :", sol.daysBetweenDates(date1, date2))
