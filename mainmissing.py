
class Solution:
    def missing_elements(self,arr):
    
        expected_sum = (n * (n+1)) // 2
        actual_sum = sum(arr)
        missing_num = expected_sum - actual_sum
        return missing_num
        
arr = []
n =int(input('enter the value'))
for i in range()
missing_num = missing_elements(arr, n)
print("Missing number is:", missing_num)