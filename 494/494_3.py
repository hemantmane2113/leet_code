class Solution:

    def uniformArray(self, nums1: list[int]) -> bool:

        p = len(nums1)

       

        # Scenario A: Try making everything ODD

        nums2 = []

        for i in range(p):

            if nums1[i] % 2 != 0:

                # Keep it if it's already odd

                nums2.append(nums1[i])

            else:

                # Even number: try to subtract a distinct odd number to make it odd

                subtracted = False

                for j in range(p):

                    if i != j and nums1[j] % 2 != 0:

                        nums2.append(nums1[i] - nums1[j])

                        subtracted = True

                        break

                if not subtracted:

                    nums2.append(nums1[i]) # Fallback if no odd number exists

 

        # Check if Scenario A succeeded (all odd)

        if all(x % 2 != 0 for x in nums2) and len(nums2) == p:

            return True

 

        # Scenario B: Try making everything EVEN

        nums2 = []

        for i in range(p):

            if nums1[i] % 2 == 0:

                # Keep it if it's already even

                nums2.append(nums1[i])

            else:

                # Odd number: try to subtract a distinct odd number to make it even

                subtracted = False

                for j in range(p):

                    if i != j and nums1[j] % 2 != 0:

                        nums2.append(nums1[i] - nums1[j])

                        subtracted = True

                        break

                if not subtracted:

                    nums2.append(nums1[i]) # Fallback if no odd number exists

 

        # Check if Scenario B succeeded (all even)

        if all(x % 2 == 0 for x in nums2) and len(nums2) == p:
            return True
        
        return False