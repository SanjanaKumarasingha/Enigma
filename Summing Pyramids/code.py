def generate_pascal_triangle(LastArray): 
    triangle = []
    triangle.append(LastArray)   
    for i in range(10):
        row = [0] * 4
        row[0] = 1
        for j in range(1, 4):
            row[j] = LastArray[j-1] + LastArray[j]
        triangle.append(row)
        LastArray = row
    return triangle

def triangle_sum(triangle):
    Sum = []
    for row in triangle:
        Sum.append(sum(row))
    return Sum

def main():
    pascal_triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4]]
    triangle_Sum = [1, 2, 4, 8, 15]
    num = int(input())

    while triangle_Sum[-1] < num:
        LastArray = pascal_triangle[-1]
        pascal_triangle = generate_pascal_triangle(LastArray)
        triangle_Sum = triangle_sum(pascal_triangle)
        # print("Pascal's Triangle:", pascal_triangle)
        # print("Sum of Pascal's Triangle:", triangle_Sum)
        # print("***************")

    for i in range(len(triangle_Sum)):
        if triangle_Sum[i] >= num:
            # print the previous number
            print(triangle_Sum[i-1])
            break


if __name__ == "__main__":
    main()
