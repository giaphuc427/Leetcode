class Solution:
    def maxProfit(self, prices) -> int:
        _min = float('inf')
        _max = 0
        store_max = []
        for idx in range(len(prices)):
            store_max.append(_max)
            _max = 0
            if prices[idx] < _min:
                _min = prices[idx]
            elif prices[idx] - _min > _max:
                _max = (prices[idx] - _min) + self.maxProfit(prices[idx+1:])

        store_max.append(_max)
        return max(store_max)

a = [1,2,3,4,5]
obj = Solution()
print(obj.maxProfit(a))
