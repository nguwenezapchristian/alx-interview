# Pascal's Triangle

## What is Pascal's Triangle

Pascals triangle or Pascal's triangle is a special triangle that is named after Blaise Pascal, in this triangle, we start with 1 at the top, then 1s at both sides of the triangle until the end. The middle numbers are so filled that each number is the sum of the two numbers just above it. The number of elements in the nth row is equal to (n + 1) elements. Pascal's triangle can be constructed by writing 1 as the first and the last element of a row and the other elements of the row are obtained from the sum of the two consecutive elements of the previous row. Pascal's triangle can be constructed easily by just adding the pair of successive numbers in the preceding lines and writing them in the new line.

## Technical Interview question

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n: 
 
    - Returns an empty list if n <= 0 
    - You can assume n will be always an integer 

## code snippet

``` To be added when I'm done ```

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