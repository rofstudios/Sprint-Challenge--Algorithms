#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
This is a linear runtime. 
a)  a = 0
    while (a < n * n * n): O(n) 
      a = a + n * n O(1)
O(n) + O(1) ~ O(n + 1) == O(n)

This while loop iterates linearly 0(n) based on n

b) O(nlogn)
b)  sum = 0
    for i in range(n): O(n)
      j = 1
      while j < n: O(logn)
        j *= 2
        sum += 1
O(n) * O(logn) == O(nlogn)

The For loop is dependant of n, making it be O(n)
The while loop is dependant of n, it is cutting down the runtime and space from fast to slightly fast making it a O(logn)

c) O(n)
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) 2
        return 2 + bunnyEars(bunnies-1) 1
          return 2 + bunnyEars(bunnies-1) 0

This function runs on itself once per bunny
this function is dependant of n making it O(n)
if we input 3 we get 6
2 we get 4
1 we get 2

## Exercise II


n = story building
f = floor
low floor = 0 
high floor = max of f
middle = ? broken or not broken egg

My current idea for solving this is by implementing a binarary search style method.
Take the total number of floors (n) from this I would find the middle floor (n/2). Knowing my middle floor, I would drop an egg and record the results. If the the egg breaks, we can elimate the current and all higher floors as the egg should theoretically break from those as well. With half the floors gone, I would find the middle floor again and drop the egg. Continue this process until the middle floor does not break the egg.

If we want to find the highest point at which we can drop the egg without breaking, we can eliminate all the previous floors under the middle that didn't break and repeat the process until the remaining values are 2, one is the highst point that it wont break and two is the lowest point at which it will break.

Because this uses a binary search method, it focuses on eliminating the process in half everytime, it is O(logn)
