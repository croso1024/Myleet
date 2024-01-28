class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # 由後往前塞入內容 
        insert_probe = m + n - 1
        probeA = m - 1 
        probeB = n - 1 

        while probeA >= 0 and probeB >= 0 : 

            if nums1[probeA] > nums2[probeB] :  
                nums1[insert_probe] = nums1[probeA] 
                insert_probe -= 1 
                probeA -= 1 
            else : 
                nums1[insert_probe] = nums2[probeB] 
                insert_probe -= 1 
                probeB -= 1 

        # 至此 , 就是只剩下 probeA或probeB 一個還有剩
        while probeA >= 0 : 
            nums1[insert_probe] = nums1[probeA]
            insert_probe -= 1 
            probeA -= 1   
        
        while probeB >= 0 : 
            nums1[insert_probe] = nums2[probeB]
            insert_probe -= 1 
            probeB -= 1   
        
        return nums1 