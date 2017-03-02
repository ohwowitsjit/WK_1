import fractions;
from functools import reduce;

print("Enter your list of numbers separated by spaces:");
nums = [int(x) for x in input().split()]
hcf= reduce(fractions.gcd, nums);

print("The Highest Common Factor is ", str(hcf));
