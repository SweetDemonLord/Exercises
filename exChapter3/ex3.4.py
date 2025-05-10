def show(A):
    for a in A:
        for i in a:
            print(i, end=' ')
        print()
def fill_snake_matrix(rows,cols):
    matrix=[[0 for i in range(cols)] for j in range(rows)]
    num=1
    top, bottom = 0, rows-1
    left, right = 0, cols-1

    while top <= bottom and left <= right:
        # Fill the upper row
        for i in range(left, right+1):
            matrix[top][i]=num
            num+=1
        top+=1
        # Fill the right column
        for i in range(top, bottom+1):
            matrix[i][right]=num
            num+=1
        right-=1

        if top<=bottom:
            # Fill the lower row
            for i in range(right, left-1, -1):
                matrix[bottom][i]=num
                num+=1
            bottom-=1
        if left<=right:
            # Fill the left column
            for i in range(bottom, top-1, -1):
                matrix[i][left]=num
                num+=1
            left+=1
    return matrix
rows,columns=eval(input("Enter a number of rows and columns:"))
A=fill_snake_matrix(rows,columns)
print("Your list:")
for rows in A:
    print(rows)