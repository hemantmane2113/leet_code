class Solution:
    def sumAndMultiply(self, n: int) -> int:

        num_list = []
        total = 0

        if n == 0:
            return 0
        if n < 0:
            n = abs(n)

        while n != 0:
            digit = n % 10
            n = n // 10
            #print(digit)
            if digit != 0:
                num_list.append(digit)
                total = total + digit
        
            #print("num to list:",num_list)
            #print(total)

        num_list_rev = []
        for i in range(len(num_list)-1,-1,-1):
            num_list_rev.append(str(num_list[i]))
        #print("num list reversed:",num_list_rev)
     
        new_num = "".join(num_list_rev)
        #print("new num:",new_num) 
        final = int(new_num) * total

        return final

def main():
    num = int(input())

    iobj = Solution()

    iRet = iobj.sumAndMultiply(num)
    print(iRet)

if __name__ == "__main__":
    main()