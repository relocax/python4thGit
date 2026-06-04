lang = 'nep'

match lang:
    case 'nep':
        print("Namaste")

    case 'eng':
        print("Hello")

    case _:
        print("Language Not Supportes")


x = int(input("Enter x: "))
y = int(input("Enter y: "))

op = input("Enter operation (1,2,3,4): ")

match op:
    case '1':
        print(x * y)

    case '2':
        print(x / y)

    case '3':
        print(x + y)

    case '4':
        print(x - y)

    case _:
        print("Invalid operation")

i = 10
while i>=1:
    print(i)
    i-=1

i=10
total= 0
while i<=10:
    if i% 2==0:
        print(i, end=" ")
    total +=1
    i+=1
print("\nTotal:", total)


i=1
j=0
while i<=10:
    i = i+j
    i+=1

print(i)

total = 0
i = 1

while i <= 10:
    total += i
    i += 1

print(total)

numbers = [12, 56, 76, 67, 87, 70]
i-0
for number in numbers:
    i += number;

print(i)

x=0
while x<len(numbers):
    print(numbers[x], end=" ")
    x+=1

for i in range(11, 1):
    print(i, end=" ")

    #duplicated values in list should be removed
    #make it ascending and desending