
count = 0
largest = float("-inf")
smallest = float("+inf")
second_largest = float("+inf")

while count < 3:
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    if (num > smallest) & (num < largest):
        num = second_largest
    count += 1

print("The largest number is", largest)
print("The second largest number is", second_largest)
