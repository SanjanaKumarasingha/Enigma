def Pascal_Triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


def main():
    pascal_triangle = Pascal_Triangle(12)
    # print("Pascal's Triangle:", pascal_triangle)
    print("*** Pascal's Triangle ***")
    for row in pascal_triangle:
        print(row)


if __name__ == "__main__":
    main()
