
'''Solution 1'''
## Brute Force I - Time Limit will Exceed
class Solution1:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        '''
        TC: O(n^2) - we will traverse the list for each element (n elements, n traversals = n*n = n^2)
        AS: O(1)
        '''
        n = len(nums)
        result = [i for i in range(1, n) if i not in nums]

        return result

nums = [4,3,2,7,8,2,3,1]        
s = Solution1()
print(s.findDisappearedNumbers(nums))

'''Solution 2'''
## Brute Force II - Sort the Array; iterate over the array and find the missing element
class Solution2:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        '''
        TC: O(nlogn) 
        AS: O(1)
        '''
        n = len(nums)
        nums = sorted(nums)
        result = []
        idx = 1
        for i in range(0, n):
            if idx != nums[i]:
                idx += 1
                if idx != nums[i]:
                    result.append(idx)
        return result
    
nums = [4,3,3,2,2,7,8,2,3,1]        
s = Solution2()
print(s.findDisappearedNumbers(nums))


'''Solution 3'''
## To reduce the search from O(n) to O(1) - we will use Hashing >> HASHSET
class Solution3:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        '''
        TC: O(n^2) - we will traverse the set for each element in O(1) search time, so for n elements it will be O(1*n) = O(n)
        AS: O(n) - converted the list into in the set and stored in memory so O(n)
        ''' 
        n = len(nums)
        nums_set = set(nums)
        result = [i for i in range(1, n) if i not in nums_set]

        return result

nums = [4,3,2,7,8,2,3,1]        
s = Solution3()
print(s.findDisappearedNumbers(nums))

'''Solution 4'''
## To reduce the AS from O(n) to O(1) - we will build hashset within array by two traversals of the array
## TC = O(n) + O(n) = O(2n) = o(n)
class Solution4:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        '''
        TC: O(n) - at i=0, nums[i] = 4, so we make the nums[nums[i]-1] = -nums[nums[i]-1], i.e, nums[4-1] = nums[3] = -nums[3]
        AS: O(1) - built a hashset within the array
        ''' 
        n = len(nums)
        result = []
        for i in range(0, n):
            value = nums[i]
            if value < 0:
                value = abs(nums[i])
            if nums[value-1] > 0:
                nums[value-1] = -nums[value-1]

        for i in range(0, n):
            if nums[i] > 0:
                result.append(i+1)

        return result


nums = [4,3,2,7,8,2,3,1]        
s = Solution4()
print(s.findDisappearedNumbers(nums))
  