class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        k = 1
        while True:
            sum_k = (k * (k + 1)) // 2
            
            if sum_k > n:
                break
            if (n - sum_k) % k == 0:
                count += 1
                
            k += 1
            
        return count