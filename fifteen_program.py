#1. Write a program to check whether a given number is even or odd.
num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#2. Write a program to check whether a given number is divisible by 5.
num = 25

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

#3. Write a program to check whether a given number is divisible by both 5 and 7.
num = 35

if num % 5 == 0 and num % 7 == 0:
    print("Divisible by both 5 and 7")
else:
    print("Not divisible by both 5 and 7")

#4. Write a program to find the largest of three numbers.
a, b, c = 10, 25, 15

if a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")

#5. Write a program to check whether a given number is positive, negative, or zero.
num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#6. Write a program to print numbers from 1 to N using a loop.
N = 10

for i in range(1, N + 1):
    print(i)

#7. Write a program to calculate the sum of first N natural numbers.
N = 10
total = 0

for i in range(1, N + 1):
    total += i

print("Sum =", total)

#8. Write a program to reverse a given number.
num = 1234
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)

#9. Write a program to check whether a given number is a palindrome.
num = 121
temp = num
reverse = 0

while temp != 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#10. Write a program to check whether a given number is a prime number.
num = 29
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime Number")

#11. Write a program to swap two numbers without using a third variable.
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print("a =", a, "b =", b)

#12. Write a program to check whether a given number is a multiple of 3 or 9.
num = 27

if num % 3 == 0 or num % 9 == 0:
    print("Multiple of 3 or 9")
else:
    print("Not a multiple of 3 or 9")

#13. Write a program to find whether a given number is divisible by 2, 3, or 4.
num = 12

if num % 2 == 0 or num % 3 == 0 or num % 4 == 0:
    print("Divisible by 2, 3, or 4")
else:
    print("Not divisible by 2, 3, or 4")

#14. Write a program to check whether a given year is a leap year or not.
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#15. Write a program to find the smallest element in a list/array.
numbers = [25, 10, 45, 5, 30]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest :", smallest)