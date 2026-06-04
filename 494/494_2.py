class Solution:

    def uniformArray(self, nums1: list[int]) -> bool:

        p = len(nums1)

       

        # STRATEGY 1: TRY TO MAKE EVERYTHING ODD

        nums2_odd = []

        for i in range(0, p):

            if nums1[i] % 2 != 0:

                nums2_odd.append(nums1[i])

            else:            

                for j in range(p):

                    if nums1[j] != nums1[i] and nums1[j] % 2 != 0: # even - odd = odd    

                        nums2_odd.append(nums1[i] - nums1[j])

                        break

                else:

                    nums2_odd.append(nums1[i])

       

        # Check if Strategy 1 succeeded (all elements are odd)

        if all(x % 2 != 0 for x in nums2_odd):

            return True

 

        # STRATEGY 2: TRY TO MAKE EVERYTHING EVEN

        nums2_even = []

        for i in range(0, p):

            if nums1[i] % 2 == 0:

                nums2_even.append(nums1[i])

            else:            

                for j in range(p):

                    if nums1[j] != nums1[i] and nums1[j] % 2 != 0: # odd - odd = even    

                        nums2_even.append(nums1[i] - nums1[j])

                        break

                else:

                    nums2_even.append(nums1[i])

 

 

        # Check if Strategy 2 succeeded (all elements are even)

        if all(x % 2 == 0 for x in nums2_even):

            return True

           

        return False
