def sortArray(arr):
    # Sử dụng thuật toán sắp xếp nổi bọt (bubble sort) để sắp xếp mảng
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def countPrime(arr):
    n=0
    for i in arr:
        if isPrime(i):
            n+=1
    return n
# Nhận một chuỗi các số nguyên từ người dùng, cách nhau bởi dấu cách
input_str = input("Enter a list of numbers separated by space: ")
# Tách chuỗi thành các chuỗi con và chuyển đổi chúng thành số nguyên
numbers = [int(num) for num in input_str.split()]
print("The list of numbers is:", numbers)
# Test the function on the first number of the list if it exists
if numbers:
    num_to_check = numbers[0]
    if isPrime(num_to_check):
        print(f"{num_to_check} is a prime number.")
    else:
        print(f"{num_to_check} is not a prime number.")
