# Brute Force
class Solution1:
    '''
    TC: O(2n) = O(n) ~~ Two comparisons at each place
    AS: O(1)
    '''
    def getMinMax(self, nums):
        minElmnt = float('inf')
        maxElmnt = float('-inf')
        for i in nums:
            if i < minElmnt:
                minElmnt = i
            if i > maxElmnt:
                maxElmnt = i
        
        print(f"Minimum element is: {minElmnt}")
        print(f"Maximum element is: {maxElmnt}")


x = Solution1()

nums1 = [3, 5, 4, 1, 9]
x.getMinMax(nums1)

nums2 = [22, 14, 8, 17, 35, 3]
x.getMinMax(nums2)


# Can reduce the iterations but can't change the TC
## This solutions needs to account for ---->>> both EVEN and ODD number of LIST
class Solution2:
    '''
    TC: O(3/2*n) = O(1.5n) = O(n) ~~ 3 comparisons * (n/2 :as we pairs ) = 3n/2 
    AS: O(1)
    '''
    def getMinMax(self, nums):
        i = 0
        n = len(nums)
        result = []

        if n%2 == 0:
            if nums[i] < nums[i+1]:
                minElmnt = nums[i]
                maxElmnt = nums[i+1]
            else:
                maxElmnt = nums[i]
                minElmnt = nums[i+1]
            start = 2
        else:
            maxElmnt = minElmnt = nums[0]
            start = 1


        for i in range(start, n, 2):
            if nums[i] < nums[i+1]: # Comparison 1
                minElmnt = min(minElmnt, nums[i]) # Comparison 2
                maxElmnt = max(maxElmnt, nums[i+1]) # Comparison 3
            else: 
                minElmnt = min(minElmnt, nums[i+1]) # Comparison 2
                maxElmnt = max(maxElmnt, nums[i]) # Comparison 3

        print(f"Minimum element is: {minElmnt}")
        print(f"Maximum element is: {maxElmnt}")
        
if __name__ == '__main__':
    y = Solution2()

    nums1 = [3, 5, 4, 1, 9]
    y.getMinMax(nums1)

    nums2 = [22, 14, 8, 17, 35, 3]
    y.getMinMax(nums2)
