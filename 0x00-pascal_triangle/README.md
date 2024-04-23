# Pascal's Triangle

## What is Pascal's Triangle

Pascals triangle or Pascal's triangle is a special triangle that is named after Blaise Pascal, in this triangle, we start with 1 at the top, then 1s at both sides of the triangle until the end. The middle numbers are so filled that each number is the sum of the two numbers just above it. The number of elements in the nth row is equal to (n + 1) elements. Pascal's triangle can be constructed by writing 1 as the first and the last element of a row and the other elements of the row are obtained from the sum of the two consecutive elements of the previous row. Pascal's triangle can be constructed easily by just adding the pair of successive numbers in the preceding lines and writing them in the new line.

## Technical Interview question

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n: 
 
    - Returns an empty list if n <= 0 
    - You can assume n will be always an integer 

## code snippet

Two ways I used to solve the challenge: 

### 1st way using list comprehension to find the exact number for each position

```
#!/usr/bin/python3
"""
A Program which generate Pascal's Triangle when given
the number of rows. It returns a list of lists of integers
representing the Pascal's triangle of n(rows)
"""


def pascal_triangle(n):
    """ returns an empty list if n <= 0 """
    triangle_list = []
    if n <= 0:
        return triangle_list
    i = 0
    while i < n:
        row = [1] * (i + 1)
        j = 1
        while j < i:
            row[j] = triangle_list[i - 1][j - 1] + triangle_list[i - 1][j]
            j += 1
        triangle_list.append(row)
        i += 1
    return (triangle_list)
```

### 2nd way using a formula to find the exact number for each position

``` 
#!/usr/bin/python3 
""" 
A Program which generate Pascal's Triangle when given 
the number of rows. It returns a list of lists of integers 
representing the Pascal's triangle of n(rows) 
""" 
 
def pascal_triangle(n): 
    triangle_list = [] 
    if n <= 0: 
        return triangle_list 
    i = 0 
    while i < n: 
        row = [] 
        j = 0 
        while j <= i: 
            if i == 0 or j == 0: 
                num = 1 
            else: 
                """ Here i used // to get integer instead of a float 
                    and this formula num = (num * (i - j + 1)) // j is 
                    used to generate the exact value on each row and column 
                """ 
                num = (num * (i - j + 1)) // j 
            row.append(num) 
            j += 1 
        triangle_list.append(row) 
        i += 1 
    return triangle_list
```

## Python file to test the program

```
#!/usr/bin/python3 
""" 
0-main 
""" 
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle 
 
def print_triangle(triangle): 
    """ 
    Print the triangle 
    """ 
    for row in triangle: 
        print("[{}]".format(",".join([str(x) for x in row]))) 
 
 
if __name__ == "__main__": 
    print_triangle(pascal_triangle(5)) 
```

## The output when i run the 0-main.py file
```
nguweneza@nguweneza-ThinkPad-T420s:~/ALX/alx-interview/0x00-pascal_triangle$ python3 0-main.py 
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
nguweneza@nguweneza-ThinkPad-T420s:~/ALX/alx-interview/0x00-pascal_triangle$ 
```
