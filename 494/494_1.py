class Solution:

    def uniformArray(self, nums1: list[int]) -> bool:

        p = len(nums1)

        nums2 = []

        even_count = 0

        odd_count = 0

       

        # count even and odd numbers

        for i in range(0, p):

            if nums1[i] % 2 == 0:  

                even_count += 1

            else:

                odd_count += 1

       

# if odd numbers are more,take odd as it is and make even odd

        if odd_count >= even_count:

            for i in range(0,p):

                if nums1[i] % 2 != 0:

                    nums2.append(nums1[i])

                else:            

                    for j in range(p):

                        if nums1[j] != nums1[i] and nums1[j] % 2 != 0: # even - odd = odd    

                            x = nums1[i] - nums1[j]

                            nums2.append(x)

                            break

                    else:

                        nums2.append(nums1[i])

                           

 # if even numbers are more ,take even numbers as it is and convert odd numbers to even                          

                   

        else:

            for i in range(0, p):

                if nums1[i] % 2 == 0:

                    nums2.append(nums1[i])

                else:            

                    for j in range (p):

                        if nums1[j] != nums1[i]  and nums1[j] % 2 != 0 :   # odd - odd = even    

                            x = nums1[i] - nums1[j]

                            nums2.append(x)

                            break

                    else:

                        nums2.append(nums1[i])

                       

        even_count = 0

        odd_count = 0

                          

       

        for i in range(0, p):

            if nums2[i] % 2 == 0:

                even_count += 1

            else:

                odd_count += 1

 

        if even_count == len(nums2) or odd_count == len(nums2):

            return True

        else:

            return False