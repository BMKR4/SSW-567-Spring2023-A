# SSW-567-Spring2023-A

HW 02a

Trianglr.py changes

1. solved the bug of invalid input
  b <= b changed to b <= 0
2. solved the bug of not a triangle
  the condition was wrong corrected it
  (a + b <= c) or (a + c <= b) or (b + c <= a)
3. added edge testcases of right angle
  (((a * 2) + (c * 2)) == (b * 2)), (((c * 2) + (b * 2)) == (a * 2))
4. solved the conditions of scalene triangle 
  added the condition, (c != a)
  
  TestTriangle.py
  
  1. case-1: the output is wrong it is right, it should be scalene
  2. case-2: the output is wrong it is right, it should be scalene
