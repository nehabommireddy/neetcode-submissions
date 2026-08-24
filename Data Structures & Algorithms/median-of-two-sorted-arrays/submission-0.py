class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        total = (len(nums1) + len(nums2))
        left = 0
        right = len(A)
        while left <= right:
            x = (left+right)//2
            y = total//2 - x

            Aleft = A[x-1] if x>0 else float('-inf')
            Aright = A[x] if x<len(A) else float('inf')
            Bleft = B[y-1] if y>0 else float('-inf')
            Bright = B[y] if y<len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if (total%2==0):
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = x - 1
            elif Bleft > Aright:
                left = x + 1

