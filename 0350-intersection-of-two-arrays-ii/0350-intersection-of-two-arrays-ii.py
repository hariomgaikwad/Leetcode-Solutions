class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_map = {}
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in freq_map:
                freq_map [nums1[i]] += 1
            else:
                freq_map[nums1[i]] = 1
        
        for i in range(len(nums2)):
            if nums2[i] in freq_map and freq_map [nums2[i]] > 0:
                ans.append(nums2[i])
                freq_map[nums2[i]] -= 1

        return ans 


        