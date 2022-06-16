# O(log(n))
def func2(n):
    if n <= 1:
        return
    else:
        print(n)
        func2(n / 2)


# O(n)
def func3(numbers):
    for num in numbers:
        print(num)


# O(n * log(n))
def func4(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    func4(n / 2)


# O(n**2)
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()

