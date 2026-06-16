class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        s = str(abs(n))
        # remove zeros
        s_no_zero = s.replace("0", "")
        if not s_no_zero:
            return 0

        total = sum(int(ch) for ch in s_no_zero)
        new_num = int(s_no_zero)
        return new_num * total

def main():
    num = int(input())

    iobj = Solution()

    iRet = iobj.sumAndMultiply(num)
    print(iRet)

if __name__ == "__main__":
    main()