# for char28 in range(33, 127):  # ASCII characters from 32 to 126
#     for char29 in range(33, 127):  # ASCII characters from 32 to 126
#         if complex(char28, char29) == complex(76, 49):
#             print("Characters for 28th and 29th positions:", chr(char28), chr(char29))
#             break

# import math

# target_value = 6640

# for num1 in range(33, 125):
#     for num2 in range(33, 125):
#         if (num1 * num2) // math.gcd(num1, num2) == target_value:
#             print("Found num1 and num2:", num1, num2)
#             break

for n in range(0, 1000):
    if (n - (83 + 80) - 100) == 0:
        print(n)
        break