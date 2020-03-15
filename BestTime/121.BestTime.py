class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 9999999
        max = 0
        for element in prices:
            if element < min:
                min = element
            elif element - min > max:
                max = element - min
        return max  