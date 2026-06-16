def finding_degree(matrix:list[list[int]])-> list[int]:
    n = len(matrix)

    ans = []
    for i in range(n):
        ans[i] = sum(matrix[i])

    return ans


def main():
    n = int(input("Enter the dimension of matrix( n*n): "))

    matrix = []
    row = []
    for i in range(1,n+1):
        print(f"Enter {n} numbers for row {i}: ")
        for j in range(1,n+1):
            num = int(input(f"Enter number {j} of {n}: "))
            row.append(num)
        matrix.append(row)
        row = []

    print(matrix)

    iret  = finding_degree(matrix)

    print("The degree of the given matrix is: ",iret)



if __name__ == "__main__":
    main()