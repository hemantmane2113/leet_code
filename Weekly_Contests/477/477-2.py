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
            
            if digit != 0:
                num_list.append(digit)
                total = total + digit
        
            

        num_list.reverse()# here the change is made from 477-1.py
        new_num_str = "".join(str(d) for d in num_list)   
        final = int(new_num_str) * total

        return final

def main():
    num = int(input())

    iobj = Solution()

    iRet = iobj.sumAndMultiply(num)
    print(iRet)

if __name__ == "__main__":
    main()